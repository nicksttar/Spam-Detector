# Spam Detector
This is a simple spam detector. For make classification model I used SVC and data with 5572 mails.

## Files
* main.py: the application file.
* spam_detection_model_results.ipynb: file with creating model.
* spam_filter.joblib: model SVC.
* spam.csv: data with 5572 mails.
* X_to_vector.csv: file need to use with model.
## Updates
### Version 1.0
- Created basic project.
## How to Use
First clone repository. Next launch file main.py and write into console mail text. Programm will show results (spam\hum) and percentage of probability. Also you need to know that this file works with english letters with 'real spam'. It means that model can't show 'hidden spam' because model was fitted using 'real spam'.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
