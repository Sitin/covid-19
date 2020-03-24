FROM python:3.7

ARG AWS_REGION
ARG AWS_SSM_ROOT_PATH
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# Set working directory to /app
RUN mkdir /app
WORKDIR /app

# Install Node.js
RUN apt-get update && apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_12.x  | bash - && apt-get -y install nodejs

# Install System Python requirements
COPY ./requirements-system.txt /app
RUN pip install -r requirements-system.txt

# Install Jupyter Hub prerequisites
RUN npm install -g configurable-http-proxy

# Install Jupyter Extensions & Widgets
COPY ./jupyter_notebook_config.py /app
COPY ./jupyterhub_config.py /app
RUN jupyter nbextension enable --py --sys-prefix widgetsnbextension && \
    jupyter nbextension enable --py --sys-prefix qgrid && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager @8080labs/qgrid

# Install R & R Jupyter kernel
RUN apt-get -y install r-base libzmq3-dev libcurl4-openssl-dev libssl-dev
RUN Rscript -e "install.packages(c('repr', 'IRdisplay', 'IRkernel'), type = 'source', repos='http://cran.r-project.org')"
RUN Rscript -e "IRkernel::installspec(user = FALSE)"

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "/tmp/awscliv2.zip" && \
    cd /tmp/ && unzip awscliv2.zip && ./aws/install && \
    rm -f /tmp/awscliv2.zip

# Install General Python requirements
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

# Fix executables
RUN chmod +x /app/bin/*.*

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Setup Jupyter
ENV JUPYTER_CONFIG_DIR=/app

# Install covid-19 module locally (turned OFF, fixed by PYTHONPATH):
#RUN python setup.py install --user

EXPOSE 8888

CMD /app/bin/run.sh
