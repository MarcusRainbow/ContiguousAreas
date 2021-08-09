# ContiguousAreas
Count contiguous areas in a two dimensional array of pixels.

Algorithm is impressively simple. Go through all blocks of four pixels, counting particular patterns. Add one for this pattern:

```
1 0
0 0
```

Subtract one for this pattern:

```
1 1
1 0
```

That's it. It counts contiguous areas of set pixels, bordered by a unset pixels.

## Why does it work?

Any rectangular block has only one bottom right hand corner (+1). If it's a fancier sort of block, it may have multiple +1 corner, but for all but one there is a matching -1 corner. For example, this figure has one +1 corner:

```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 0 0
0 0 1 1 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```

Think about adding one set pixel anywhere around this block, to create another +1 corner. There are only two places where this is possible:


```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 1 b 0
0 0 1 1 0 0
0 0 a 0 0 0
0 0 0 0 0 0
```

I have marked these as 'a' and 'b'. Adding either of these results in two +1 corners. However, it also adds a -1 corner. You can see how this can result in a proof by induction that any simply connected shape results in a count of one.

Clearly, shapes that are not connected are additive. Thus the overall count is a count of simply connected shapes.

(apologies for the hand-wavy maths)

## Is there anything special about top-left and bottom-right

No, the algorithm also works equally well with any opposing pair of corners, for example add one for this pattern:

```
0 1
0 0
```

Subtract one for this pattern:

```
1 1
0 1
```



