FROM python:3.9

# Prepare tests
ADD features features
ADD requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Installing Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update && apt-get install -y google-chrome-stable

CMD ["behave"]
