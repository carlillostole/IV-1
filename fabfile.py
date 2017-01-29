from fabric.api import *
import os

def descargar():
    run ('sudo rm -rf IV')
    run ('sudo git clone https://github.com/sergiocaceres/IV')

def detener():
    run ("sudo supervisorctl stop comuni_bot")

def borrar():
    run ('sudo rm -rf IV')

def instalar():
    run ('cd IV && make install')

def recargar():
    run("sudo supervisorctl reload")

def iniciar():
    with shell_env(TOKENBOT=os.environ['TOKENBOT'], USR_BD=os.environ['USR_BD'], PASS_BD=os.environ['PASS_BD']):
        run('sudo supervisorctl start comuni_bot')

def iniciar_no_supervisor():
    with shell_env(TOKENBOT=os.environ['TOKENBOT'], USR_BD=os.environ['USR_BD'], PASS_BD=os.environ['PASS_BD']):
        run('cd IV && make execute')

def iniciar_hup():
    with shell_env(TOKENBOT=os.environ['TOKENBOT'], USR_BD=os.environ['USR_BD'], PASS_BD=os.environ['PASS_BD']):
        run ('nohup python IV/bot_telegram/bot.py >& /dev/null &',pty=False)
