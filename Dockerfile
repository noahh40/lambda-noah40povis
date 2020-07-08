FROM debian# Comments are like this
# So logging works w/Docker
ENV PYTHONUNBUFFERED=1# You can RUN things, mostly to install dependencies
RUN apt-get update && apt-get upgrade -y && \
  apt-get install python3-pip -y && \
  pip3 install pandas && \
  pip3 install -i https://pypi.org/project/lambdata-noah40povis/ lambda-noah40povis && \
  python3 -c "import lambdata_noah40povis; print(lambdata_noah40povis.TEST)"