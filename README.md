# Firebase Service Account Token Generator

---

## This repository provides a Python script to generate an Access Token for Firebase services using a Service Account JSON key. Access tokens are essential for authenticating and interacting with Firebase services via REST APIs or other tools.

---

## Overview

Firebase services require an access token for authentication when performing operations outside the Firebase Admin SDK. This script simplifies the process of generating OAuth 2.0 access tokens using a service account key file.
It leverages the google-auth library to interact with Google Cloud's authentication system and allows you to request an access token for specific scopes.

---

## Features

- Easy-to-use Python script to generate access tokens.
- Supports custom OAuth 2.0 scopes.
- Automatically refreshes the token as needed.
- Works with the Service Account JSON key provided by Google Cloud.

---

## How to use?

Change the SERVICE_ACCOUNT_FILE to the correct destination of the file

NOTE: Make sure it's the destination including the file! 
-Example: 
- ✅ C:/Users/You/Desktop/FIREBASE-PROJECT-firebase-adminsdk-hhwin-af156ed22p.json
- ❌ C:/Users/You/Desktop/

---

## Contributing

Contributions are welcome! If you find any issues or want to add features, feel free to submit a pull request or open an issue.

---

## Contact

For questions or suggestions, please contact the repository owner. 🚀
Github: juliuspleunes4
LinkedIn: www.linkedin.com/in/juliuspleunes
