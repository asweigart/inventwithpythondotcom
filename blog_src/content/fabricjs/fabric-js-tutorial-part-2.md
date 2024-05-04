Title: Fabric.js Tutorial Part 2
Date: 2024-05-04 10:02
Authors: Al Sweigart
Summary: Part 2 of a tutorial series on the Fabric.js canvas/graphics library for JavaScript, where we learn about Polyline shapes and styling shapes by drawing a gingerbread figure.

<script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>

This is Part 2 of the Fabric.js tutorial. You can start at the beginning with [Part 1]({filename}fabric-js-tutorial-part-1.md).

Drawing a Gingerbread Figure
====================

Let's learn about a new shape, polyline, and how to add styling such as rounded corners and rotation by drawing this gingerbread figure:

<canvas id="gingerbreadCanvasId" width="200" height="200" style="border: 1px solid black;"></canvas>

<script>
// Create a Fabric.js "Canvas" object that is tied to the HTML <canvas> element:
let canvasObj = new fabric.Canvas('gingerbreadCanvasId');

const GINGERBREAD_COLOR = '#CD803D';

let head = new fabric.Circle({
  left: 100, top: 50, fill: GINGERBREAD_COLOR, radius: 40, originX: 'center', originY: 'center'
})


let arms = new fabric.Polyline(
  [{x: 0, y: 0}, {x: 100, y:0}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, strokeLineCap: 'round', fill: 'transparent', left: 100, top: 100, originX: 'center', originY: 'center'
  });

let legs = new fabric.Polyline(
  [{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, strokeLineCap: 'round', fill: 'transparent', left: 100, top: 140, originX: 'center', originY: 'center'
  });

let leftEye = new fabric.Circle({
  left: 90, top: 40, fill: 'transparent', stroke: 'white', radius: 10, originX: 'center', originY: 'center'
});

let rightEye = new fabric.Circle({
  left: 110, top: 40, fill: 'transparent', stroke: 'white', radius: 5, originX: 'center', originY: 'center'
});

let mouth = new fabric.Rect({
  left: 100, top: 70, originX: 'center', originY: 'center', fill: 'transparent', stroke: 'white', strokeWidth: 6, width: 40, height: 10, rx: 5, ry: 5, angle: 15
});

let topButton = new fabric.Circle({
  left: 100, top: 90, originX: 'center', originY: 'center', radius: 4, fill: 'black', stroke: 'black'
});

let bottomButton = new fabric.Circle({
  left: 100, top: 110, originX: 'center', originY: 'center', radius: 4
});

canvasObj.add(head);
canvasObj.add(arms);
canvasObj.add(legs);
canvasObj.add(leftEye);
canvasObj.add(rightEye);
canvasObj.add(mouth);
canvasObj.add(topButton);
canvasObj.add(bottomButton);
</script>

The full code is at [https://inventwithpython.com/fabric-js-tutorial/fabric-js-gingerbread-figure.html](https://inventwithpython.com/fabric-js-tutorial/fabric-js-gingerbread-figure.html) or on [JSFiddle](https://jsfiddle.net/asweigart/7kxv10f9/). Let's examine each part individually:


```
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Fabric.js Gingerbread Figure</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/fabric.js/5.3.1/fabric.min.js"></script>
</head>

<body>
  <!-- The HTML <canvas> element: -->
  <canvas id="gingerbreadCanvasId" width="200" height="200" style="border: 1px solid black;"></canvas>
</body>
```

Again, this is the standard HTML boilerplate that we have for our page but I include it to have a complete example that is viewable in an actual web browser. Note that the ID of the &lt;canvas&gt; element is `"gingerbreadCanvasId"`.

<hr>

```
<script>
// Create a Fabric.js "Canvas" object that is tied to the HTML <canvas> element:
let canvasObj = new fabric.Canvas('gingerbreadCanvasId');

const GINGERBREAD_COLOR = '#CD803D';

let head = new fabric.Circle({
  left: 100, top: 50, fill: GINGERBREAD_COLOR, radius: 40, originX: 'center', originY: 'center'
})
```

Multiple shapes use the color `#CD803D` so let's save it to the constant `GINGERBREAD_COLOR`. We'll create a new `fabric.Circle` object for the gungerbread figure's head. Notice that because the `originX` and `originY` properties are set to `'center'`, the `left` and `top` settings refer to the X and Y coordinates of the shape's *center point* and not the top-left corner. Confusingly, we still have to use the `left` and `top` property names.

<hr>

```
let arms = new fabric.Polyline(
  [{x: 0, y: 0}, {x: 100, y:0}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, strokeLineCap: 'round', fill: 'transparent', left: 100, top: 100, originX: 'center', originY: 'center'
  });

let legs = new fabric.Polyline(
  [{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, strokeLineCap: 'round', fill: 'transparent', left: 100, top: 140, originX: 'center', originY: 'center'
  });
```

To create the arms and legs, we'll use a new shape called polyline which represents a connected series of lines. The first argument to the `fabric.Polyline` is an array of objects with `x` and `y` properties.

The arms only have two points: `[{x: 0, y: 0}, {x: 100, y:0}]` These X and Y coordinates *can* be relative to the shape's own Cartesian coordinate system, and then the shape is position on the &lt;canvas&gt; element with the `left` and `top` properties.

You *can alternatively* use the &lt;canvs&gt; element's coordinate system (where the 0, 0 origin is the top-left corner of the &lt;canvas&gt; element) for the array of points and then leave the `left` and `top` properties as their default `0` and `0` values.

The legs are made from a second polyline that has three points: `[{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}]`

The color and thickness of the polyline is set by the `stroke` and `strokeWidth` properties in this object. Setting the stroke color to `GINGEBREAD_COLOR` gives us the following shapes:

<canvas id="gingerbreadCanvas2Id" width="200" height="200" style="border: 1px solid black;"></canvas>

<script>
// Create a Fabric.js "Canvas" object that is tied to the HTML <canvas> element:
let canvasObj2 = new fabric.Canvas('gingerbreadCanvas2Id');

let arms2 = new fabric.Polyline(
  [{x: 0, y: 0}, {x: 100, y:0}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 1, fill: 'transparent', left: 100, top: 100, originX: 'center', originY: 'center'
  });

let legs2 = new fabric.Polyline(
  [{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 1, fill: 'transparent', left: 100, top: 140, originX: 'center', originY: 'center'
  });

canvasObj2.add(arms2);
canvasObj2.add(legs2);
</script>

Adding a `strokeWidth` of `40` makes these lines thicker:


<canvas id="gingerbreadCanvas3Id" width="200" height="200" style="border: 1px solid black;"></canvas>
<script>
// Create a Fabric.js "Canvas" object that is tied to the HTML <canvas> element:
let canvasObj3 = new fabric.Canvas('gingerbreadCanvas3Id');

let arms3 = new fabric.Polyline(
  [{x: 0, y: 0}, {x: 100, y:0}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, fill: 'transparent', left: 100, top: 100, originX: 'center', originY: 'center'
  });

let legs3 = new fabric.Polyline(
  [{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, fill: 'transparent', left: 100, top: 140, originX: 'center', originY: 'center'
  });

canvasObj3.add(arms3);
canvasObj3.add(legs3);
</script>

However, to give the gingerbread figure a more rounded look, we set the `strokeLineCap` to `'round'`. (It can also be set to `'square'` or `'butt'`, with the default being `'butt'`.)

<canvas id="gingerbreadCanvas4Id" width="200" height="200" style="border: 1px solid black;"></canvas>

<script>
// Create a Fabric.js "Canvas" object that is tied to the HTML <canvas> element:
canvasObj = new fabric.Canvas('gingerbreadCanvas4Id');

arms = new fabric.Polyline(
  [{x: 0, y: 0}, {x: 100, y:0}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, fill: 'transparent', left: 100, top: 100, originX: 'center', originY: 'center', strokeLineCap: 'round'
  });

legs = new fabric.Polyline(
  [{x: 0, y: 60}, {x: 30, y: 0}, {x: 60, y: 60}], {
    stroke: GINGERBREAD_COLOR, strokeWidth: 40, fill: 'transparent', left: 100, top: 140, originX: 'center', originY: 'center', strokeLineCap: 'round'
  });

canvasObj.add(arms);
canvasObj.add(legs);
</script>

Note that setting `strokeLineCap` only applies to the two ends and not for the middle connecting points of the polyline. The connection between the two line segments in the legs polyline can also be rounded if you set the `strokeLineJoin` property to `'round'`. (It can also be set to `'bevel'` or `'miter'`, with the default being `'miter'`.)

It may seem odd that a polyline has a `fill` property, but the area that is filled in is described by the *polygon shape* that a polyline draws. The complete shape includes connecting the end point to the start point. By default, the fill color is black. To make the fill invisible and only draw a line, we must set `fill` to `'transparent'`.

Later we'll use a `fabric.Polygon` shape, which is the same thing as `fabric.Polyline` but its stroke connects the last point back to the first point.

<hr>

```
let mouth = new fabric.Rect({
  left: 100, top: 70, originX: 'center', originY: 'center', fill: 'transparent', stroke: 'white', strokeWidth: 6, width: 40, height: 10, rx: 5, ry: 5, angle: 15
});
```

The mouth is a white rectangle outline, but we give it rounded corners by setting the horiztonal and vertical radius of the corners with `rx` and `ry` to 5 pixels. The rectangle is also rotated counter-clockwise by 15 degrees by setting `angle` to `15`. Note that this rotation is specified in number of degrees and not number of radians.

<hr>

```
let leftEye = new fabric.Circle({
  left: 90, top: 40, fill: 'transparent', stroke: 'white', radius: 10, originX: 'center', originY: 'center'
});

let rightEye = new fabric.Circle({
  left: 110, top: 40, fill: 'transparent', stroke: 'white', radius: 5, originX: 'center', originY: 'center'
});

let topButton = new fabric.Circle({
  left: 100, top: 90, originX: 'center', originY: 'center', radius: 4, fill: 'black', stroke: 'black'
});

let bottomButton = new fabric.Circle({
  left: 100, top: 110, originX: 'center', originY: 'center', radius: 4
});
```

The last shapes are four circles for the eyes and buttons. These use the same concepts we have seen before.

<hr>

```
canvasObj.add(head);
canvasObj.add(arms);
canvasObj.add(legs);
canvasObj.add(leftEye);
canvasObj.add(rightEye);
canvasObj.add(mouth);
canvasObj.add(topButton);
canvasObj.add(bottomButton);
</script>
```

Finally, none of these shapes will appear on the canvas until we call the `add()` method for each of them.

This tutorial continues on to [Part 3]({filename}fabric-js-tutorial-part-3.md). Special thanks to [Hunor Márton Borbély](https://bio.link/hunor) for the [SVG tutorial](https://svg-tutorial.com/svg/gingerbread-figure) that inspired this Fabric.js tutorial.