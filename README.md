# generate-avatar

Generates an avatar image given a seed. For the same input you should get the same avatar.

## Examples

![test1](https://github.com/txrvictor/generate-avatar/assets/75559055/4ef2e2ff-191b-4fa8-be08-5021c52a195d) ![test2](https://github.com/txrvictor/generate-avatar/assets/75559055/5c1891b5-6ce0-4c14-9b41-e0580de96f58) ![test3](https://github.com/txrvictor/generate-avatar/assets/75559055/c75923b7-063b-41af-934f-f352dd9095eb) ![test4](https://github.com/txrvictor/generate-avatar/assets/75559055/bdb3eb5c-2286-43cf-a8b6-8345e43c826a) ![test5](https://github.com/txrvictor/generate-avatar/assets/75559055/37c7a46c-858d-4150-b31b-ca38ecf7834b) ![test6](https://github.com/txrvictor/generate-avatar/assets/75559055/74391a52-da8f-478e-bf5a-9f9259c7ef53) ![test7](https://github.com/txrvictor/generate-avatar/assets/75559055/68fc7392-8f2d-4ebc-bfd8-0c7075dc22a7) ![test8](https://github.com/txrvictor/generate-avatar/assets/75559055/04d47eef-1f9a-4efa-a61d-e7b5579bd903)


## Help & Options

To check the available options you can run:
```
python3 main.py -h
```

| Options       | Description                                                   | Example      |
| ------------- |---------------------------------------------------------------| -------------|
| -c            | Pixel Color                                                   | '#a1b2c3'    |
| -bg           | Background Color                                              | '#a1b2c3'    |
| -f            | Name of the file to be saved, otherwise it displays the image | 'avatar.png' |


### How to run from command line

1) Clone the repo

2) Change to the repo's directory:
```
cd generate-avatar
```

3) Create virtual environment:
```
python3 -m venv venv
```

4) Activate the virtual environment:
```
source venv/bin/activate
```

5) Install requirements for the venv:
```
pip3 install -r requirements.txt
```

6) Run the app:
```
python3 main.py "some seed string for generating an avatar image"
```
