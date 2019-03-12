# # Simple REST Full API of Luthvi Riskawati's Research

Research documentation

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed Python 3 on your device

### Project structure
```
* flask-rest-api/
  |--- app/
  |    |--- constant/
  |    |    |--- __init__.py
  |    |    |--- StringConstant.py
  |    |--- controller/
  |    |    |--- __init__.py
  |    |    |--- AppController.py
  |    |--- db/
  |    |    |--- dataset-pre.xlsx
  |    |    |--- datasets.xlsx
  |    |--- module/
  |    |    |--- __init__.py
  |    |    |--- AppModule.py
  |    |--- static/
  |    |    |--- images/
  |    |    |--- js/
  |    |--- templates/
  |    |    |--- index.html
  |    |--- __init__.py
  |--- docs/
  |--- venv/
  |--- run.py
```
### Project Description

1. Constant directory, used to constant string as Relevant or Irrelevant string, etc.
2. Controller directory, used to handling request from http request both web or API Request
3. Db directory, used to save datasets from upload data if not exists you should create before run this project
4. Module directory, used to functionality or logic process in this research then called from controller
5. Static directory, used to serve css or javascript files
6. Templates directpry, used for html file when called from controller
7. Docs directory, used to save documentation of this research
8. Venv directory, used for virtual environment on this app with python3

### Step to run flask rest api

A step by step series of examples that tell you how to get a development env running

1. Install virtual environment
```
pip install virtualenv
```
2. Create virtual environment and activate inside your flask-rest-api directory according the above structure
```
virtualenv venv
> On windows -> venv\Scripts\activate
> On linux -> . env/bin/activate
```
3. Install some third party librares on your virtual environment with pip
```
pip install -r requirements.txt
```
4. Run web service
```
python run.py
```
5. Then access from browser `http://localhost:8000/`
![Sample 1](https://github.com/whatyourdream/mine/blob/master/docs/1.PNG)

6. Then upload your latest dataset into form upload
![Sample 2](https://github.com/whatyourdream/mine/blob/master/docs/2.PNG)


### How to request data from API Request or Postman

1. On postman, change request to POST then fill in url to ```http://localhost:8000/api/get-result`
2. Choose `body` menu to create body request, then choose `raw` and `application/json` type
3. Create body request, then click `Send` button
```JSON
{
	"query": "daging ayam makaroni tahu"
}
```
4. You should have response like below
```JSON
{
    "columns": [
        "Bahan",
        "Score",
        "Information"
    ],
    "data": [
        [
            ", 350 cc Air, 50 gram Daging Ayam, 50 gram Nasi Aron, 20 gram Tahu, 20 gram Wortel",
            0.5454545455,
            "Relevant"
        ],
        [
            "25 gram Daging Ayam, 25 gram Kacang Polong, 300 cc Kaldu, 10 gram Keju Parut, 25 gram Makaroni, 25 gram Tahu Potong, 25 gram Tomat",
            0.5333333333,
            "Relevant"
        ],
        [
            "120 ml Air, 25 gram Brokoli, 40 gram Daging Ayam Tanpa Lemak, 200 gram Kentang, 100 gram Tahu, 40 gram Wortel",
            0.5,
            "Relevant"
        ],
        [
            "2 sendok makan Beras, 25 gram Daging Ayam, 300 ml Kaldu Ayam, 10 gram Keju Parut, 200 ml Santan, 25 gram Tahu, 25 gram Tomat, 5 gram Wortel",
            0.4,
            "Irrelevant"
        ],
        [
            "250 ml Air, 25 gram Buncis Potong Kecil, 30 gram Daging Ayam, 100 gram Kentang, 25 gram Tahu Potong Kecil, 25 gram Wortel Iris Halus",
            0.3529411765,
            "Irrelevant"
        ],
        [
            "60 ml ASI, 40 gram Daging Tuna, 1/2 sendok makan Daun Seledri, 100 ml Kaldu Ayam, 60 gram Kentang",
            0.3333333333,
            "Irrelevant"
        ],
        [
            "250 cc Air, 35 gram Brokoli, 35 gram Daging Ayam Cincang, 50 gram Keju Parut, 50 gram Macaroni",
            0.3333333333,
            "Irrelevant"
        ],
        [
            ", 2 sendok makan Beras Putih, 1 sendok makan Daging Ayam Giling, 750 ml Kaldu Sapi, 50 gram Tempe, 25 gram Wortel",
            0.3076923077,
            "Irrelevant"
        ],
        [
            "50 gram Bayam, 100 gram Daging Sapi, 100 gram Makaroni, 1 butir telur, 2 sendok makan Margarin, 75 cc Susu Cair, 50 gram Wortel",
            0.3076923077,
            "Irrelevant"
        ],
        [
            "10 gram Bayam, 10 gram Daging Ayam, 125 ml Kaldu, 10 gram Kentang, 1 butir Kuning Telur, 10 gram Tomat, 10 gram Wortel",
            0.3076923077,
            "Irrelevant"
        ],
        [
            "25 gram Bayam, 50 gram Daging Ayam Giling, 50 gram Jagung Muda, 625 ml Kaldu Ayam, 1 sendok teh Mentega, 50 gram Tempe",
            0.2857142857,
            "Irrelevant"
        ],
        [
            "50 gram Brokoli, 75 gram Daging Sapi Cincang, 50 gram Keju Cheddar, 1/2 sendok makan Mentega, 75 gram Tahu, 75 gram Tomat Merah",
            0.2857142857,
            "Irrelevant"
        ],
        [
            "25 gram Bayam, 25 gram Daging Ayam Cincang, 250 ml Kaldu Ayam, 10 gram Keju, 100 gram Kentang, 25 gram Tempe, 25 gram Wortel",
            0.2857142857,
            "Irrelevant"
        ],
        [
            "300 ml Air Kaldu, 1 sendok makan Bawang Bombay, 1 siung Bawang Putih, 80 gram Brokoli, 50 gram Daging Ayam, 1 sendok teh Garam, 1/3 sendok teh Gula Pasir, 1 sendok makan Margarin, 1 buah Tahu Cina, 2 sendok makan Tepung Beras, 1 buah Tomat",
            0.2727272727,
            "Irrelevant"
        ],
        [
            "1 siung Bawang Putih, 50 gram Daging Ayam, 25 gram Keju Parut, 100 gram Kembang Kol, 100 gram Kentang, 1/2 sendok teh Mentega Tawar",
            0.2666666667,
            "Irrelevant"
        ],
        [
            "1 siung Bawang Putih, 50 gram Daging Ayam, 25 gram Keju Parut, 100 gram Kembang Kol, 100 gram Kentang, 1/2 sendok teh Mentega Tawar",
            0.2666666667,
            "Irrelevant"
        ],
        [
            "1 sendok teh Bawang Bombay, 50 gram Brokoli, 50 gram Dada Ayam, 200 ml Kaldu Ayam, 50 gram Kentang, 1 sendok teh Minyak Zaitun, 50 gram Tahu Sutra",
            0.25,
            "Irrelevant"
        ],
        [
            "1 buah Apel, 250 ml Kaldu Ayam, 30 gram Kentang, 30 gram Wortel",
            0.2222222222,
            "Irrelevant"
        ],
        [
            "100 gram Kacang Polong, 100 ml Kaldu Ayam, 100 gram Wortel",
            0.2222222222,
            "Irrelevant"
        ],
        [
            "3 gelas Air Kaldu Ayam, 2 sendok makan Brokoli, 2 sendok makan Daging Ayam, 1 buah Jagung Manis Parut, 1 mangkok Kecil Nasi, 2 sendok makan Keju Parut",
            0.2105263158,
            "Irrelevant"
        ],
        [
            "50 gram Ayam, 50 gram Brokoli, 100 ml Kaldu Ayam, 50 gram Labu Kuning",
            0.2,
            "Irrelevant"
        ],
        [
            "30 ml Air, 30 gram Buncis, 50 gram Daging Cincang, 50 gram Kentang, 1 sendok makan Margarin",
            0.2,
            "Irrelevant"
        ],
        [
            "300 ml Susu Kedelai, 50 gram Tahu, 50 gram Tempe, 2 sendok makan Tepung Maizena",
            0.2,
            "Irrelevant"
        ],
        [
            "500 cc Air, 50 gram Beras, 50 gram Daging Sapi, 50 gram Jamur, 1 sendok makan Minyak Sayur",
            0.1818181818,
            "Irrelevant"
        ],
        [
            "1 cangkir Asi, 1 buah Dada Ayam Tanpa Tulang Dan Kulit, 1/2 sendok teh Tepung Maizena",
            0.1818181818,
            "Irrelevant"
        ],
        [
            "100 ml ASI, 75 ml Air, 100 gram Daging Jambu Biji, 100 gram Tepung Beras Merah",
            0.1666666667,
            "Irrelevant"
        ],
        [
            "50 gram Bayam, 20 gram Beras Merah, 25 gram Hati Ayam, 150 ml Kaldu, 1 sendok teh Margarin Tawar, 50 gram Terong",
            0.1538461538,
            "Irrelevant"
        ],
        [
            "100 cc ASI, cc Air Matang, 25 gram Bayam Merah, 150 cc Kaldu Ayam, 25 gram Ubi Ungu",
            0.1538461538,
            "Irrelevant"
        ],
        [
            "Air Matang secukupnya, 100 gram Daging Buah Avokad, 1 buah Pisang Ambon, 100 cc Susu Formula",
            0.1538461538,
            "Irrelevant"
        ],
        [
            "1/2 sendok teh Garam Halus, 500 cc Kaldu, 10 gram Margarin, 50 gram Tahu, 20 gram Tepung Beras, 50 gram Tomat, 40 gram Wortel",
            0.1538461538,
            "Irrelevant"
        ],
        [
            "600 ml Air, 30 gram Brokoli, Cincang, 30 gram Daging Ikan Tuna, 1 sendok makan Minyak Zaitun, 50 gram Wortel",
            0.1538461538,
            "Irrelevant"
        ],
        [
            "10 lembar Daun Bayam Merah, 200 ml Kaldu Daging Sapi, 50 gram Tempe, 100 gram Tepung Beras",
            0.1428571429,
            "Irrelevant"
        ],
        [
            "50 gram Beras, 25 gram Brokoli, 1/2 sendok teh Garam, 400 cc Kaldu Ayam, 2 sendok teh Minyak, 50 gram Tempe, 15 gram Teri Nasi Tawar",
            0.1428571429,
            "Irrelevant"
        ],
        [
            "500 ml Air Kaldu, 20 sendok makan Beras Merah, 20 gram Brokoli, 20 gram Hati Ayam, 20 gram Keju Parut, 20 gram Wortel",
            0.1428571429,
            "Irrelevant"
        ],
        [
            "15 gram Bawang Bombay, 50 gram Beras, 100 gram Daging Sapi Cincang, 1 lembar Daun Salam, 1 sendok teh Garam, 2 sendok teh Garam, 1 sendok teh Kaldu Ayam Bubuk, 375 ml Kaldu Ikan, 1 sendok makan Kecap Jepang, 1/2 sendok makan Kecap Manis, 1/2 sendok teh Merica Bubuk, 1 sendok makan Minyak Sayur, 35 g",
            0.1379310345,
            "Irrelevant"
        ],
        [
            "500 cc Air, 1 siung Bawang Putih, 100 gram Bayam, 100 gram Beras, 100 gram Daging Ikan Gabus Segar, 1/2 sendok teh Garam, 2 buah Wortel",
            0.1333333333,
            "Irrelevant"
        ],
        [
            ", 20 gram Beras, 10 gram Daun Bayam, 25 gram Hati Ayam, 10 gram Kacang Hijau, 20 gr Tomat, 20 gr Wortel",
            0.1333333333,
            "Irrelevant"
        ],
        [
            "1/2 sendok teh Bawang Bombay, 50 gram Daging Sapi Cincang, 1 sendok makan Margarin, 200 ml Susu Kedelai, 50 gram Tepung Terigu, 10 gram Wortel, Rebus",
            0.125,
            "Irrelevant"
        ],
        [
            "1 Kuning telur, 25 gram Bayam Merah, 2 sendok makan Beras Merah, 25 gram Daging Sapi, 450 ml Kaldu Sapi, 200 ml Santan, 25 gram Tomat",
            0.125,
            "Irrelevant"
        ],
        [
            "5 buah Bakso, 1 batang Bawang Daun, 1 siung Bawang Putih, 1 sendok teh Garam, 500 cc Kaldu, 1 sendok makan Minyak Sayur, 1 buah Oyong, 1 batang Seledri, 50 gram Soun, 1 buah Tahu",
            0.1176470588,
            "Irrelevant"
        ],
        [
            "15 gram Daging Ikan Tenggiri, 30 gram Jagung Manis, 150 cc Kaldu, 25 gram Kangkung, 1 sendok makan Mentega, 50 gram Nasi Aron, 1 tangkai Seledri, 25 gram Tomat",
            0.1176470588,
            "Irrelevant"
        ],
        [
            "400 ml Air Kaldu Ikan, 50 gram Daging Ikan Salmon, 1 butir Kuning Telur, 300 gram Labu Kuning, 1 sendok makan Reju Ricotta, 50 gram Tempe",
            0.1176470588,
            "Irrelevant"
        ],
        [
            "100 ml Air Kaldu Ayam, 100 gram Nasi Aron Setengah Matang, 1/2 sendok teh Seledri (cincang Halus), 4 buah Telur Puyuh, 50 gram Wortel",
            0.1176470588,
            "Irrelevant"
        ],
        [
            ", 25 gram Beras Merah, 15 gram Brokoli, 15 gram Daging Sapi, 15 gram Kembang Kol, 1 butir Kuning Telur, 50 cc Santan Encer, 1 sendok makan Tepung Beras",
            0.1176470588,
            "Irrelevant"
        ],
        [
            "1 siung Bawang Putih, 50 gram Daging Giling, 50 gram Jagung Serut, 1 sendok teh Mentega Tawar, 75 gram Nasi Tim, 25 gram Sawi Hijau, 25 gram Wortel Parut",
            0.1111111111,
            "Irrelevant"
        ],
        [
            ", 1 siung Bawang Putih, 1 sendok teh Garam, 1 buah Hati Ayam Rebus, 50 gram Jagung Manis, 200 ml Kaldu Ayam, 1 sendok teh Mentega, 50 ml Susu, 1 sendok teh Tepung Terigu, 20 gram Wortel",
            0.1052631579,
            "Irrelevant"
        ],
        [
            "45 gram Beras, 40 gram Daging Ikan Gurame, 25 gram Daun Bayam, 45 gram Kacang Hijau, 500 ml Kaldu Ikan Gurame, 2 butir Kuning Telur, 120 ml Santan, 25 gram Tomat, 25 gram Wortel",
            0.1,
            "Irrelevant"
        ],
        [
            "1/4 siung Bawang Putih, 25 gram Daun Bayam, 50 gram Hati Sapi, 100 ml Kaldu Kaki Ayam, 50 gram Labu Siam, 1/2 sendok teh Minyak Wijen, 100 gram Nasi Aron, 25 gram Wortel Parut",
            0.0952380952,
            "Irrelevant"
        ],
        [
            "1 batang daun seledri, 25 gram Bawang Bombay, 50 gram Daging Giling, 20 ml Jus Apel, 40 ml Kaldu Sapi, 15 gram Keju Chedar, 1/2 sendok teh Mentega Tawar, 1 sendok teh Tepung Terigu, 30 gram Tomat, 50 buah Wortel",
            0.0909090909,
            "Irrelevant"
        ],
        [
            "1 batang daun seledri, 25 gram Bawang Bombay, 50 gram Daging Giling, 20 ml Jus Apel, 40 ml Kaldu Sapi, 15 gram Keju Chedar, 1/2 sendok teh Mentega Tawar, 1 sendok teh Tepung Terigu, 30 gram Tomat, 50 buah Wortel",
            0.0909090909,
            "Irrelevant"
        ],
        [
            "400 ml Air, 1 sendok teh Air Jeruk Lemon, 1 butir Bawang Merah, 1 siung Bawang Putih, 50 gram Beras Merah, 25 gram Daging Ikan Tenggiri, 4 lembar Daun Seledri, 1 sendok makan Margarin, 1 sendok makan Udang, 20 gram Wortel",
            0.0869565217,
            "Irrelevant"
        ],
        [
            "150 gram Ayam, 1/2 buah Bawang Bombay, 2 siung Bawang Putih, 5 batang Buncis, 1 sendok teh Garam, 1/2 sendok teh Gula, 1 buah Jagung Manis, 1 sendok makan Margarin, 100 ml Susu Cair, 2 butir Telur, 100 gram Tepung Roti, 2 sendok makan Tepung Terigu, 1 buah Wortel",
            0.0869565217,
            "Irrelevant"
        ],
        [
            "5 cm kayumanis, 100 cc Air, 75 gram Bawang Bombay, 1 siung Bawang Putih, 100 gram Beras, 2 butir Cengkih, 150 gram Daging Ikan Kakap, 1/2 sendok teh Garam, 1/4 sendok teh Gula Pasir, 4 sendok makan Minyak Goreng, 250 gram Paprika Merah, 1 butir Pekak, 100 gram Tomat Merah",
            0.0769230769,
            "Irrelevant"
        ],
        [
            "1 putih telur, kocok lepas, 1 sendok makan Air Jeruk Nipis, 3 siung Bawang Merah, 3 siung Bawang Putih, 200 gram Daging Ikan Tenggiri, 1 lembar Daun Bawang, Iris Halus, secukupnya Garam, 200 gram Kentang Kupas, Kukus Matang, Dinginkan Lalu Haluskan, 1 sendok teh Ketumbar Sangrai, secukupnya Minyak S",
            0.0540540541,
            "Irrelevant"
        ],
        [
            "1 helai daun pandan, 50 ml Air, 1/8 sendok teh Garam, 100 gram Gula Merah, 2 sendok makan Gula Pasir, 500 ml Minyak Goreng, 5 buah Ubi Merah, 1 sendok makan Wijen Putih Sangrai",
            0,
            "Irrelevant"
        ],
        [
            "1/4 sendok teh merica, 1/2 sendok teh Garam, 1/2 sendok makan Kacang Polong Beku, 1 sendok makan Keju Parut, 1/2 sendok makan Margarin, 50 gram Nasi Putih, 1 butir Telur",
            0,
            "Irrelevant"
        ],
        [
            "100 cc ASI, 200 cc Air Hangat, 30 gram Tepung Kacang Hijau, 1 buah tomat",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air Matang, 100 gram Jagung Manis, 25 gram Keju Parut, 1 butir Kuning Telur, 3 sendok makan Susu Bubuk",
            0,
            "Irrelevant"
        ],
        [
            "200 ml Air Matang, 2 sendok makan Madu Murni, 1 buah Pisang Ambon, 100 gram Stroberi",
            0,
            "Irrelevant"
        ],
        [
            "1/2 sendok teh Garam, 750 gram Kentang, 3 sendok teh Margarin, 1 sendok teh Merica Bubuk, 1/2 sendok teh Pala Bubuk, 225 ml Susu Cair",
            0,
            "Irrelevant"
        ],
        [
            ", 1/2 sendok teh Garam, 300 ml Minyak Goreng, 2 lembar Roti Tawar, 1 butir Telur, 100 gram Udang",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Asi, 25 gram Bayam, 50 gram Ubi",
            0,
            "Irrelevant"
        ],
        [
            "2 buah Air Jeruk Manis Untuk Saus, 100 gram Belimbing, 3 sendok makan Madu Untuk Saus, 100 gram Melon, 100 gram Nanas, 100 gram Semangka, 12 buah Tusukan Sate",
            0,
            "Irrelevant"
        ],
        [
            "150 ml Air, 30 gram Buncis, 50 gram Kentang, 30 gram Teri Basah, 25 gram Tomat",
            0,
            "Irrelevant"
        ],
        [
            "200 ml Air, 30 gram Bayam, 30 gram Beras Putih, 30 gram Tuna",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air Jeruk Manis, 200 ml Air Matang Hangat, 1/2 buah Apel, 50 gram Tepung Beras",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air Perasan Jeruk Manis, 1 buah Naga Merah, 200 gram Semangka",
            0,
            "Irrelevant"
        ],
        [
            "1 batang Daun Bawang, 1 sendok teh Garam Halus, 500 gram Kentang, 100 gram Kornet Kalengan, 1 sendok makan Margarin",
            0,
            "Irrelevant"
        ],
        [
            "50 gram Keju Parut, 2 buah Pisang Ambon, 3 lembar Roti Tawar Gandum, 150 cc Susu Cair",
            0,
            "Irrelevant"
        ],
        [
            "1 buah Jagung Manis, 100 gram Kacang Polong, 50 gram Keju Cheddar, 125 gram Margarin, 1/2 sendok teh Merica Bubuk, 200 ml Susu Cair, 2 butir Telur, 350 gram Tepung Terigu, 100 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            ", 100 ml Air, 1 sendok teh Gula Merah, 100 gr Jagung Muda Pipilan, 3 sendok takar Susu Formula",
            0,
            "Irrelevant"
        ],
        [
            "30 gram Bayam, 25 gram Butter Tawar, 30 gram Daun Bawang, 25 gram Kacang Polong Beku, 200 ml Kaldu, 25 gram Ubi",
            0,
            "Irrelevant"
        ],
        [
            "50 ml ASI, 200 ml Air, 50 ml Air Jeruk Manis, 20 gram Tepung Beras, 2 sendok makan Tepung Maizena",
            0,
            "Irrelevant"
        ],
        [
            "75 cc Air, 100 ml Asi, 50 gram Buah Apel, 50 gram Buah Pir, 1 sendok makan Tepung Maizena",
            0,
            "Irrelevant"
        ],
        [
            "200 ml Air, 30 gram Melon, 20 gram Susu Bubuk Formula, 20 gram Tepung Beras",
            0,
            "Irrelevant"
        ],
        [
            "200 ml Air Panas, 30 gram Bayam Merah, 50 gram Ikan Kakap, 150 gram Labu Kuning, 1 sendok makan Margarin",
            0,
            "Irrelevant"
        ],
        [
            "200 cc Air Jeruk Manis, 1 buah Pisang Ambon",
            0,
            "Irrelevant"
        ],
        [
            "300 cc Air, 100 gram Fillet Kakap, Potong Kecil-kecil, 1/8 sendok teh Garam, 75 gram Kacang Polong, 100 gram Labu Kuning, Potong Dadu, 75 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            "50 gram Ikan Salmon, 200 ml Kaldu Ikan, 50 gram Kentang",
            0,
            "Irrelevant"
        ],
        [
            "50 gram Alpukat Matang, 100 ml Susu Formula, 20 gram Tepung Beras Merah",
            0,
            "Irrelevant"
        ],
        [
            ", 100 cc ASI, 200 cc Air, 50 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            "150 cc ASI, 100 cc Air Matang, 1 sendok teh Gula Pasir Halus, 70 gram Jagung Manis",
            0,
            "Irrelevant"
        ],
        [
            "50 cc ASI, 50 gram Stroberi",
            0,
            "Irrelevant"
        ],
        [
            "200 cc Air Matang Hangat, 1 buah Pisang Ambon, 2 lembar Roti Tawar, 4 sendok takar Susu Formula",
            0,
            "Irrelevant"
        ],
        [
            "50 gram Bayam, 50 gram Ikan Dori, 100 ml Kaldu Ikan, 50 gram Keju Parut, 1 buah Kentang, 1 sendok teh Tepung Maizena",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air, 50 gram Havermut Instan, 50 gram Pepaya, 150 ml Susu Cair",
            0,
            "Irrelevant"
        ],
        [
            "115 gram Brokoli, 175 gram Kentang, 300 cc Susu Formula Cair, 115 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            "100 cc Air Masak Hangat, 50 gram Aprikot, 100 cc Asi Perah, 50 gram Pepaya, 3 sendok takar Peres Susu Formula, 40 gram Promina Beras Merah",
            0,
            "Irrelevant"
        ],
        [
            "50 ml Air, 1/4 sendok teh Kayumanis, 2 buah Pisang Ambon",
            0,
            "Irrelevant"
        ],
        [
            "1 butir kuning telur, 50 gram Gula Kastor, 75 gram Keju Cheddar, 130 gram Mentega Tawar, 25 gram Tepung Jagung, 150 gram Tepung Terigu",
            0,
            "Irrelevant"
        ],
        [
            "1/2 buah Jeruk Baby, 1 buah Pisang Ambon",
            0,
            "Irrelevant"
        ],
        [
            "100 ml ASI , 200 ml Air, 50 gram Buah Naga, 1 buah Pisang Ambon",
            0,
            "Irrelevant"
        ],
        [
            "100 ml ASI, 50 ml Air Jeruk Manis, 100 ml Air Matang, 50 gram Mangga, 50 gram Melon",
            0,
            "Irrelevant"
        ],
        [
            "150 cc Air, 100 gram Pisang Ambon, 150 cc Susu Formula, ",
            0,
            "Irrelevant"
        ],
        [
            "2 sendok makan Madu, 50 gram Maizena, 1 buah Pisang Ambon, 250 cc Susu Cair, 50 gram Tepung Hunkue",
            0,
            "Irrelevant"
        ],
        [
            "50gram Anggur, 5 sendok makan ASI, 10gram Kacang Merah",
            0,
            "Irrelevant"
        ],
        [
            "200 ml Air, 5 gram Gula Pasir, 50 gram Pepaya, 10 gram Sari Sirsak, 3 sendok makan Susu Formula Bubuk, 20 gram Tepung Maizena",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air, 1 lembar Daun Pandan, 1 buah Jagung Manis, 2 sendok makan Oatmeal",
            0,
            "Irrelevant"
        ],
        [
            "600 ml Air, 20 gram Beras, 50 gram Kentang Potong Dadu, 1 batang Seledri Iris Halus, 50 gram Teri Nasi Basah Cuci Lalu Tririskan, 25 gram Wortel Parut",
            0,
            "Irrelevant"
        ],
        [
            "60 bayam, 2 siung Bawang Putih, 2 butir Telur, 1 butir Telur, 250 gram Tempe, 50 gram Tepug Terigu, 50 gram Tepung Panir, 1 sendok makan Tepung Terigu",
            0,
            "Irrelevant"
        ],
        [
            "1 sendok teh Bumbu Spekuk, 200 gram Gula Pasir Halus, 130 gram Margarine, 1/2 sendok teh Soda Kue, 1 sendok teh Susu Bubuk, 2 butir Telur, 30 gram Terigu, 200 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            ", 350 gram Buah Pir, 3 butir Kuning Telur, 300 gram Mentega, 250 gram Susu Formula, 1 butir Telur, 600 gram Tepung Terigu, 1/2 sendok teh Vanili",
            0,
            "Irrelevant"
        ],
        [
            "200 gram Melon Kuning, 100 cc Susu Formula Cair",
            0,
            "Irrelevant"
        ],
        [
            "100 ml ASI, 100 ml Air Matang, 2 sendok makan Jeruk Manis, 4 buah Kurma, 1 buah Pisang Ambon",
            0,
            "Irrelevant"
        ],
        [
            "200 cc Air, 1 sendok makan Maizena, 70 gram Melon Kuning, 3 sendok makan Susu Formula Bubuk",
            0,
            "Irrelevant"
        ],
        [
            "100 ml Air Matang, 150 ml Air Panas, 100 ml Asi, 1 buah Kiwi, 30 gram Sereal Instan",
            0,
            "Irrelevant"
        ],
        [
            "100 ml ASI, 30 gram Jagung Manis, 200 ml Kaldu, 50 gram Kentang, 50 gram Wortel",
            0,
            "Irrelevant"
        ],
        [
            "1 sendok makan Air Jeruk Manis, 200 cc Air Matang Hangat, 50 gram Pepaya, 200 cc Susu Formula, 50 gram Tepung Beras Merah ",
            0,
            "Irrelevant"
        ],
        [
            "100 cc ASI, 100 cc Air Matang, 100 gram Kentang",
            0,
            "Irrelevant"
        ],
        [
            "100 gram Avokad, 1 sendok teh Gula Pasir, 200 cc Susu Formula Cair",
            0,
            "Irrelevant"
        ],
        [
            "150 ml Air Jeruk Manis, 100 gram Pepaya",
            0,
            "Irrelevant"
        ],
        [
            "150 ml ASI, 3 sendok makan Air Jeruk Manis, 50 gram Mangga, 1 buah Pisang Ambon Kecil",
            0,
            "Irrelevant"
        ]
    ]
}
```
