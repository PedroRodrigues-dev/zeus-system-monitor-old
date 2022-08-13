# ZEUS SYSTEM MONITOR V0.0.2
## _Sistema gerenciador de infraestrutura_
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=LICENÇA&message=MIT&color=GREEN&style=for-the-badge)
**Free Software**
## Ferramentas para desenvolvimento
- Python 3.10.4
- Sqlite3

## Funções
- Monitoramento de CPU, Memória e Disco com sensores reguláveis
- Envio de dados por amqp e armazenamento em log (configurável, padrão em log)
- Interface de comando própria para alterar configurações do ambiente'

## Instalação e configuração
### Distribuição
Apenas para linux

Variáveis de ambiente
```sh
cp .env.sample .env
```
Inicialização.
```sh
./main
```
## Desenvolvimento
Multiplataforma

Variáveis de ambiente
```sh
cp .env.sample .env
```
Preparação de ambiente
```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
Inicialização.
```sh
python main.py
```
# Compilação
Será compilado para a plataforma que está utilizando
```sh
cxfreeze main.py --target-dir dist 
```
Altere para a branch para 'dist', copie o conteúdo da pasta 'dist' para a raiz do projeto,
apague as pastas desnecessárias para o projeto compilado e envie para o github.
# Manusear configurações de ambiente
As configurações são armazenadas em sqlite3 no arquivo chamado por padrão de cfg.sqlite3,
elas podem ser alteradas por meio do shell do sistema
```sh
show
```
Exibe todos os valores de ambiente seguindo o padrão abaixo.
('time_notification_limit', '300')
('notification_destination', 'logging')
('cpu_overload_counter_limit', '30')
('cpu_percent_limit', '90')
('cpu_overload_message', 'CPU com utilizacao acima de {}%')
('memory_overload_counter_limit', '30')
('memory_percent_limit', '90')
('memory_overload_message', 'Memoria com utilizacao acima de {}%')
('disk_overload_counter_limit', '30')
('disk_percent_limit', '90')
('monitored_disk_location', '/')
('disk_overload_message', 'Disco com utilizacao acima de {}%')
('rabbit_host', 'localhost')
('rabbit_queue', 'zeus')
('thread_sleep_time', '0.6')
```sh
update
```
Atualiza as variáveis.
Digite o nome da variável e o valor e confirme que deseja realmente alterar.

**Por: Pedro Rodrigues**
![Badge Github](https://img.shields.io/github/followers/PedroRodrigues-dev?style=social)