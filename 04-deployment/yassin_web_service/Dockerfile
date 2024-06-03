FROM python:3.10.12-slim

workdir ./app

Run pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir certifi

COPY predict.py ./
copy lin_reg.bin ./
COPY requirments.txt ./
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirments.txt

expose 9696
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]