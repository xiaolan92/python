# MapLibreGLJS 学习笔记

显示卫星地图
```
const map = new maplibregl.Map({
    container: 'map',
    zoom: 9,
    center: [137.9150899566626, 36.25956997955441],
    pitch: 60, // 俯仰角（度）
    bearing: -60, // 方位角（度）
    style: {
        "version": 8,
        "sources": {
            "satellite": {
                "type": "raster",
                "tiles": [
                    "https://tiles.maps.eox.at/wmts/1.0.0/s2cloudless-2020_3857/default/g/{z}/{y}/{x}.jpg"
                ],
                "tileSize": 256
            }
        },
        "layers": [{
            "id": "satellite",
            "type": "raster",
            "source": "satellite"
        }]
    }
});


```
***
查看全屏地图
```
map.addControl(new maplibregl.FullscreenControl());

```
***

向地图添加缩放和旋转控件

```
map.addControl(new maplibregl.NavigationControl({
      visualizePitch: true,
      visualizeRoll: true,
      showZoom: true,
      showCompass: true
    }));
```

