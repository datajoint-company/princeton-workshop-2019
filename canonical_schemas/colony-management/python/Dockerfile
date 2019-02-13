FROM datajoint/jupyter:python3.6

ADD . /src/pipeline

RUN pip install -e /src/pipeline
RUN pip install gspread oauth2client
