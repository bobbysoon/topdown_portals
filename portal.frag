#version 120

uniform vec2 iResolution;
uniform vec2 view_center;

uniform vec2 l1p1,l1p2,l2p1,l2p2;
uniform float doPortal;

vec2 hash( vec2 p ) {
	p = vec2( dot(p,vec2(127.1,311.7)),
			dot(p,vec2(269.5,183.3)) );

	return -1.0 + 2.0*fract(sin(p)*43758.5453123);
}

float noise( in vec2 p ) {
	const float K1 = 0.366025404; // (sqrt(3)-1)/2;
	const float K2 = 0.211324865; // (3-sqrt(3))/6;

	vec2 i = floor( p + (p.x+p.y)*K1 );
	
	vec2 a = p - i + (i.x+i.y)*K2;
	vec2 o = (a.x>a.y) ? vec2(1.0,0.0) : vec2(0.0,1.0); //vec2 of = 0.5 + 0.5*vec2(sign(a.x-a.y), sign(a.y-a.x));
	vec2 b = a - o + K2;
	vec2 c = a - 1.0 + 2.0*K2;

	vec3 h = max( 0.5-vec3(dot(a,a), dot(b,b), dot(c,c) ), 0.0 );

	vec3 n = h*h*h*h*vec3( dot(a,hash(i+0.0)), dot(b,hash(i+o)), dot(c,hash(i+1.0)));

	return dot( n, vec3(70.0) );
	
}

float FractalNoise( vec2 p ) {
	vec2 uv = p*vec2(iResolution.x/iResolution.y,1.0);

	float f = 0.0;

	uv *= 5.0;
	mat2 m = mat2( 1.6,  1.2, -1.2,  1.6 );
	f  = 0.5000*noise( uv ); uv = m*uv;
	f += 0.2500*noise( uv ); uv = m*uv;
	f += 0.1250*noise( uv ); uv = m*uv;
	f += 0.0625*noise( uv ); uv = m*uv;


	f = 0.5 + 0.5*f;
	f *= smoothstep( 0.0, 0.005, abs(p.x-0.6) );	
	
	return f;
}

bool SegSegIntersect( vec2 s1p1,vec2 s1p2 , vec2 s2p1,vec2 s2p2 , out vec2 i) {
	//Make sure the lines aren't parallel
	float x21=s1p2.x-s1p1.x, y21=s1p2.y-s1p1.y;
	float x43=s2p2.x-s2p1.x, y43=s2p2.y-s2p1.y;
	if (y21/x21 != y43/x43) {
		float d = x21*y43 - y21*x43;
		if (d != 0) {
			float y13=s1p1.y-s2p1.y,x13=s1p1.x-s2p1.x;
			float r = (y13*x43 - x13*y43) / d;
			float s = (y13*x21 - x13*y21) / d;
			if ( r>=0 && r<=1 && s>=0 && s<=1 ) {
				i.x= s1p1.x + r*x21;
				i.y= s1p1.y + r*y21;
				return true;
			}
		}
	}
	return false;
}

/*
	LineLineIntersect	pass
	LineRayIntersect	if (s >= 0)
	LineSegIntersect	if (s >= 0 and s <= 1)
	RayLineIntersect	if (r >= 0)
	RayRayIntersect		if (r >= 0 and s >= 0)
	RaySegIntersect		if (r >= 0 and s >= 0 and s <= 1)
	SegLineIntersect	if (r >= 0 and r <= 1)
	SegRayIntersect		if (r >= 0 and r <= 1 and s >= 0)
	SegSegIntersect		if (r >= 0 and r <= 1 and s >= 0 and s <= 1)
*/

#define Dot(u,v)   (u.x*v.x + u.y*v.y)
#define Norm(v)     sqrt(v.x*v.x + v.y*v.y)     // norm = length of  vector

//	VecSegDist(): get the distance of a point to a segment
float VecSegDist( vec2 p, vec2 s1,vec2 s2) {
	vec2 v = s2-s1;
	vec2 w = p - s1;

	float c1 = Dot(w,v);
	if ( c1 <= 0 )	return Norm( vec2(p-s1) );

	float c2 = Dot(v,v);
	if ( c2 <= c1 )	return Norm( vec2(p-s2) );

	float b = c1 / c2;
	vec2 Pb = s1 + b * v;
	return Norm( vec2(p-Pb) );
}

bool thisSide(vec2 p, vec2 p1, vec2 p2) { // which side? trial end error
	return (0.0<sign((p2.x - p1.x) * (p.y - p1.y) - (p2.y - p1.y) * (p.x - p1.x)));
}

float atan2(vec2 v) {return atan(v.x,v.y);}

vec2 PortalPoint( vec2 p,vec2 i , vec2 p1,vec2 p2 , vec2 t1,vec2 t2 ) { // center-pixel , intersected portal , projection portal
	//return p;
	vec2 pi=p-i,p21=p2-p1,t21=t1-t2 , i2;
	float a,d,o;
	a= atan2(pi)-atan2(p21); // projection angle, relative to portal line
	d= length(pi)/length(p21); // projection length, relative to portal line
	o= length(i-p1)/length(p21); // intersect position, relative to portal line
	a+= atan2(t21);
	i2= t2+(t21)*o;
	return i2 + d*vec2(sin(a),cos(a))*length(t21);
}

void main() {
	vec2 p=gl_TexCoord[0].xy ;
	vec2 c1=p,c2=p;
	bool t1=false,t2=false;
	if (doPortal>0) {
		if (thisSide(p,l1p1,l1p2)) t1= SegSegIntersect( view_center,p , l1p1,l1p2 , c1);
		if (thisSide(p,l2p1,l2p2)) t2= SegSegIntersect( view_center,p , l2p1,l2p2 , c2);
	}

	float f,d=-1;
	if (t1 && t2) {
		float d1= VecSegDist(p,l1p1,l1p2);
		float d2= VecSegDist(p,l2p1,l2p2);
		if (d1>d2) {
			p= PortalPoint(p,c1 , l1p1,l1p2 , l2p1,l2p2);
			d= d1;
		} else {
			p= PortalPoint(p,c2 , l2p1,l2p2 , l1p1,l1p2);
			d= d2;
		}

		f= FractalNoise(p);
	} else {
		if (t1) {
			d= VecSegDist(p,l1p1,l1p2);
			p= PortalPoint(p,c1 , l1p1,l1p2 , l2p1,l2p2);
		} else if (t2) {
			d= VecSegDist(p,l2p1,l2p2);
			p= PortalPoint(p,c2 , l2p1,l2p2 , l1p1,l1p2);
		}

		f= FractalNoise(p);
	}

	gl_FragColor= vec4(vec3(f),1);
}
