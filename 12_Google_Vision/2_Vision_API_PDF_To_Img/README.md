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
      - [Install From Requirements](#install-from-requirements)
  - [Google Vision API](#google-vision-api)
    - [Packages](#packages)
    - [Environment Variables](#environment-variables)

# PYTHON GOOGLE VISION API

## Links

[Go Back to Contents](#contents)

- [Google Cloud Console](https://console.cloud.google.com/)
- [Pip Google Cloud Vision](https://pypi.org/project/google-cloud-vision/)
- [Pip pdf2image](https://pypi.org/project/pdf2image/)
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

  ```Bash
    pip3 freeze > requirements.txt
  ```

  - This will generate a new file `requirements.txt` with all the package that we installed in our virtual environment

#### Install From Requirements

[Go Back to Contents](#contents)

- To install the packages from `requirements.txt`

  ```Bash
    pip3 install -r requirements.txt
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

      # install google cloud vision
      pip install google-cloud-vision

      # install pdf2image
      pip install pdf2image
    ```

### Environment Variables

[Go Back to Contents](#contents)

- [https://cloud.google.com/vision/docs/before-you-begin](https://cloud.google.com/vision/docs/before-you-begin)
- We need to import the `ServiceAccountKey.json` in our python application

  ```Python
    import os

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'serviceAccountKey.json'
  ```
