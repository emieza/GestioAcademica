

from models import *
from webapp import flask_app

from multiprocessing import Process
from time import sleep

from selenium import webdriver

def before_all(context):
    print("Starting webserver...")
    context.proc = Process(target=flask_app.run)
    context.proc.start()
    sleep(1)
    print("Test thread started...")
    context.firefox = webdriver.Firefox()

def after_all(context):
    # tanquem firefox de selenium
    context.firefox.quit()
    # tanquem webserver
    context.proc.terminate()
    context.proc.join()
    print("...terminated!")


def before_feature(context,feature):
    context.classe = Classe()

