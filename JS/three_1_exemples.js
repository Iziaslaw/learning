new THREE.BoxGeometry(width : Float 1, height : Float 1, depth : Float 1, widthSegments : Integer 1, heightSegments : Integer 1, depthSegments : Integer 1)
CapsuleGeometry  (radius : Float 1, length : Float 1, capSubdivisions : Integer 4, radialSegments : Integer 8)
CircleGeometry   (radius : Float 1, segments : Integer 32, thetaStart : Float 0, thetaLength : Float PI*2)
ConeGeometry     (radius : Float 1, height : Float 1, radialSegments : Integer 32, heightSegments : Integer 1, openEnded : Boolean false, thetaStart : Float 0, thetaLength : Float PI*2)
CylinderGeometry (radiusTop : Float 1, radiusBottom : Float 1, height : Float 1, radialSegments : Integer 32, heightSegments : Integer 1, openEnded : Boolean false, thetaStart : Float 0, thetaLength : Float PI*2)
DodecahedronGeometry(radius : Float 1, detail : Integer 0)
IcosahedronGeometry(radius : Float 1, detail : Integer 0)
LatheGeometry(points : Array, segments : Integer 12, [param:Float phiStart 0], phiLength : Float PI*2)
OctahedronGeometry(radius : Float 1, detail : Integer 0)
PlaneGeometry(width : Float 1, height : Float 1, widthSegments : Integer 1, heightSegments : Integer 1)
PolyhedronGeometry(vertices : Array, indices : Array, radius : Float, detail : Integer)
RingGeometry(innerRadius : Float 0.5, outerRadius : Float 1, thetaSegments : Integer 32, phiSegments : Integer 1, thetaStart : Float 0, thetaLength : Float PI*2)
SphereGeometry(radius : Float 1, widthSegments : Integer 3, heightSegments : Integer 32, phiStart : Float 2, phiLength : Float 6, thetaStart : Float 0, thetaLength : Float 0)
TetrahedronGeometry(radius : Float 1, detail : Integer 0)
TorusGeometry(radius : Float 1, tube : Float 0.4, radialSegments : Integer 12, tubularSegments : Integer 48, arc : Float PI*2)
TorusKnotGeometry(radius : Float 1, tube : Float 0.4, tubularSegments : Integer 64, radialSegments : Integer 8, p : Integer 2, q : Integer 3)


TubeGeometry(path : Curve, tubularSegments : Integer 64, radius : Float 1, radialSegments : Integer 8, closed : Boolean false)
const path = new CustomSinCurve( 10 );

ExtrudeGeometry(shapes : Array, options : Object)
const shapes = new THREE.Shape(); shape.moveTo( 0,0 ); shape.lineTo( 0, width ); shape.lineTo( length, width ); shape.lineTo( length, 0 ); shape.lineTo( 0, 0 );
const options = {steps: 2,depth: 16,bevelEnabled: true,bevelThickness: 1,bevelSize: 1,bevelOffset: 0,bevelSegments: 1};

ShapeGeometry(shapes : Array, curveSegments : Integer)
const heartShape = new THREE.Shape();
heartShape.moveTo( x + 5, y + 5 ); heartShape.bezierCurveTo( x + 5, y + 5, x + 4, y, x, y ); heartShape.bezierCurveTo( x - 6, y, x - 6, y + 7,x - 6, y + 7 ); heartShape.bezierCurveTo( x - 6, y + 11, x - 3, y + 15.4, x + 5, y + 19 ); heartShape.bezierCurveTo( x + 12, y + 15.4, x + 16, y + 11, x + 16, y + 7 ); heartShape.bezierCurveTo( x + 16, y + 7, x + 16, y, x + 10, y ); heartShape.bezierCurveTo( x + 7, y, x + 5, y + 5, x + 5, y + 5 );