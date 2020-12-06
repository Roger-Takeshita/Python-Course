<h1 id='contents'>Table of Contents</h1>

- [PYTHON GOOGLE VISION API](#python-google-vision-api)
  - [Links](#links)
  - [Google Cloud Vision](#google-cloud-vision)
    - [New Project](#new-project)
    - [Enabling Vision](#enabling-vision)
    - [Credentials](#credentials)
  - [Python Virtual Environment](#python-virtual-environment)
    - [New Virtual Env](#new-virtual-env)
    - [Activate Virtual Env](#activate-virtual-env)
    - [Deactivate Virtual Env](#deactivate-virtual-env)
    - [Freeze Requirements](#freeze-requirements)
  - [Google Vision API](#google-vision-api)
    - [Packages](#packages)
    - [Environment Variables](#environment-variables)
    - [Code](#code)

# PYTHON GOOGLE VISION API

## Links

[Go Back to Contents](#contents)

- [Google Cloud Console](https://console.cloud.google.com/)
- [Pip Google Cloud Vision](https://pypi.org/project/google-cloud-vision/)
- [Vision - Detect text in images](https://cloud.google.com/vision/docs/ocr)

## Google Cloud Vision

### New Project

[Go Back to Contents](#contents)

- On `Google Cloud Console`

  - On the **navbar**, Click on the dropdown menu, next to **Google Cloud Platform**

    ![](https://i.imgur.com/R3SbqRQ.png)

  - Click on **NEW PROJECT**

    ![](https://i.imgur.com/bEKbMXS.png)

  - On **New Project** Page

    - Project name: `Image-Vision`
    - Location: `No organization`
    - Click on **CREATE**

      ![](https://i.imgur.com/JK27cvu.png)

### Enabling Vision

[Go Back to Contents](#contents)

- After creating your new project, select the project on the navbar

  ![](https://i.imgur.com/pWqsN0Y.png)

- On the **sidebar menu**, go to `APIs & Services > Library`

  ![](https://i.imgur.com/bxbHAOd.png)

  - Search for **Vision**

    - Select **Cloud Vision API**

      ![](https://i.imgur.com/jBBNq4N.png)

  - Click on **Cloud Vision API**

    ![](https://i.imgur.com/CHv1hKs.png)

    ![](https://i.imgur.com/QZVcIRV.png)

  - Then click on **ENABLE**

### Credentials

[Go Back to Contents](#contents)

- On the **sidebar menu**, go to `APIs & Services > Credentials`

  ![](https://i.imgur.com/VHdT81p.png)

- Click on **+ CREATE CREDENTIALS**

  ![](https://i.imgur.com/M4YFNSw.png)

- On `Create service account` page

  - Service account details

    - Service account name: `Vision API Service Account`
    - Service account description: `Gives Access to Vision API`
    - Click on **CREATE**

      ![](https://i.imgur.com/0zN4bXS.png)

  - Grant this service account access to the project

    - Select a role: `Project > Owner`
    - Click on **CONTINUE**

      ![](https://i.imgur.com/lkcuMPE.png)

      ![](https://i.imgur.com/8CG0eq6.png)

  - Grant users access to this service account (optional)

    - Leave it blank
    - Click on **DONE**

      ![](https://i.imgur.com/ozvHV1Q.png)

- On `Credentials` page

  - Click on your new service account `vision-api-service-account@image-vision-297814.iam.gserviceaccount.com`

    ![](https://i.imgur.com/hJCCPzK.png)

- On `Vision API Service Account` page

  - Click on **ADD KEY > Create new key**

    ![](https://i.imgur.com/QhQonYO.png)

  - Create private key for 'Vision API Service Account'

    - Key type: `JSON`
    - Click on **CREATE**

      ![](https://i.imgur.com/vnyZuJb.png)

      - This action will automatically download a json file containing your private key

        ![](https://i.imgur.com/Fr6J0vX.png)

## Python Virtual Environment

### New Virtual Env

[Go Back to Contents](#contents)

- On `Terminal`

  - Create a new python virtual environment inside the project's folder

    ```Bash
      python -m venv .
    ```

### Activate Virtual Env

[Go Back to Contents](#contents)

- On `Terminal`

  ```Bash
    source bin/activate
  ```

### Deactivate Virtual Env

[Go Back to Contents](#contents)

- On `Terminal`

  ```Bash
    deactivate
  ```

### Freeze Requirements

[Go Back to Contents](#contents)

- To generate the installation package, run the following command inside our virtual environment

  - `pip3 freeze > requirements.txt`
  - This will generate a new file `requirements.txt` with all the package that we installed in our virtual environment

    ```Bash
      cachetools==4.1.1
      certifi==2020.12.5
      chardet==3.0.4
      google-api-core==1.23.0
      google-auth==1.23.0
      google-cloud==0.34.0
      google-cloud-vision==2.0.0
      googleapis-common-protos==1.52.0
      grpcio==1.34.0
      idna==2.10
      libcst==0.3.15
      mypy-extensions==0.4.3
      proto-plus==1.11.0
      protobuf==3.14.0
      pyasn1==0.4.8
      pyasn1-modules==0.2.8
      pytz==2020.4
      PyYAML==5.3.1
      requests==2.25.0
      rsa==4.6
      six==1.15.0
      typing-extensions==3.7.4.3
      typing-inspect==0.6.0
      urllib3==1.26.2
    ```

## Google Vision API

[Go Back to Contents](#contents)

- Paste the API Key that we downloaded from google's website inside our project's folder
- Rename it to `serviceAccountKey.json` and add to your `.gitignore` file

### Packages

[Go Back to Contents](#contents)

- On `Terminal`

  - We need to install the google vision api library

    ```Bash
      # upgrade pip version
      python3 -m pip install --upgrade pip

      # install google cloud
      pip install google-cloud

      # install google cloud vision
      pip install google-cloud-vision
    ```

### Environment Variables

[Go Back to Contents](#contents)

- [https://cloud.google.com/vision/docs/before-you-begin](https://cloud.google.com/vision/docs/before-you-begin)
- We need to import the `ServiceAccountKey.json` in our python application

  ```Python
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceAccountKey.json'
  ```

### Code

- In `python_vision_api.py`

  ```Python
    import os
    import io
    from google.cloud import vision

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceAccountKey.json'
    client = vision.ImageAnnotatorClient()

    FILE_NAME = 'images/002.jpeg'

    with io.open(FILE_NAME, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
  ```

  ```Bash
    "DOLLAR M MENU
    MCDOUBLE
    $1 MCCHICKEN
    $1
    PARFAIT
    $1 SIDE SALAD
    $1
    SMALL FRIES
    $1 SMALL SOFT DRINK $1
    2 PIES
    $1 SUNDAE
    $1
    OPPLE DIPPERS
    $1 3 COOKIES
    $1
    "
    bounds: (95,-11),(969,-11),(969,582),(95,582)

    "DOLLAR"
    bounds: (256,52),(492,24),(497,67),(261,95)

    "M"
    bounds: (522,19),(574,13),(580,68),(528,74)

    "MENU"
    bounds: (642,5),(777,-11),(783,44),(648,60)

    "MCDOUBLE"
    bounds: (108,170),(317,147),(321,187),(113,211)

    "$1"
    bounds: (472,128),(524,122),(528,162),(477,168)

    "MCCHICKEN"
    bounds: (532,124),(787,95),(791,128),(536,158)

    "$1"
    bounds: (934,75),(961,73),(963,104),(936,106)

    "PARFAIT"
    bounds: (99,271),(253,254),(256,285),(102,302)

    "$1"
    bounds: (477,231),(504,228),(507,257),(480,260)

    "SIDE"
    bounds: (528,222),(618,211),(622,243),(532,254)

    "SALAD"
    bounds: (638,209),(772,193),(776,227),(642,243)

    "$1"
    bounds: (931,177),(960,175),(962,206),(933,208)

    "SMALL"
    bounds: (103,367),(231,353),(235,384),(106,398)

    "FRIES"
    bounds: (252,351),(362,339),(366,372),(256,384)

    "$1"
    bounds: (474,325),(523,320),(527,356),(478,362)

    "SMALL"
    bounds: (532,322),(651,309),(654,338),(535,351)

    "SOFT"
    bounds: (670,307),(770,296),(774,326),(673,337)

    "DRINK"
    bounds: (787,295),(901,283),(904,311),(790,324)

    "$1"
    bounds: (936,277),(965,274),(968,307),(940,310)

    "2"
    bounds: (95,465),(117,463),(120,494),(98,496)

    "PIES"
    bounds: (135,460),(220,451),(223,484),(138,493)

    "$1"
    bounds: (463,420),(517,414),(521,457),(467,463)

    "SUNDAE"
    bounds: (526,419),(689,402),(693,436),(529,453)

    "$1"
    bounds: (932,379),(960,378),(961,409),(933,410)

    "OPPLE"
    bounds: (101,556),(219,548),(221,574),(103,582)

    "DIPPERS"
    bounds: (238,541),(403,530),(405,566),(241,578)

    "$1"
    bounds: (467,516),(521,511),(525,554),(471,559)

    "3"
    bounds: (530,517),(553,515),(556,548),(533,550)

    "COOKIES"
    bounds: (574,511),(760,495),(763,529),(577,546)

    "$1"
    bounds: (936,480),(965,479),(966,510),(937,511)
  ```
