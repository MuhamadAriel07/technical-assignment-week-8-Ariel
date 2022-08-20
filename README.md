> Kalian diminta untuk membuat sebuah backend services untuk menerima sebuah data kecepatan, latitude dan longitude dalam sebuah body json. Dan kalian juga diharapkan untuk menyimpan data tersebut beserta dengan timestampnya.

### Expected Body
```json
{
    "kecepatan": 90,
    "latitude": 6.2088,
    "longitude": 106.8456
}
```

### Expected data yang disimpan dalam database mongodb
* ID transaksi
* kecepatan
* latitude
* longitude
* timestamp
