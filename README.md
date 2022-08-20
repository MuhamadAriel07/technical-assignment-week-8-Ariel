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

## Jawab
1. Untuk script json disimpan di file ```mainjson.py```
2. Expected body menggunakan Postman
![postman](https://user-images.githubusercontent.com/90564840/185732909-fac0fe2b-feff-40e1-ac12-3efb67a98639.PNG)

3. Untuk script menyimpan data ke mongodb disimpan di file ```db_test.py```
4. Tampilan di web ```mongodb```
![mongodb](https://user-images.githubusercontent.com/90564840/185732926-cc255311-e7e2-4643-8e4b-8061b2a03be6.PNG)
