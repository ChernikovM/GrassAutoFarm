# Grass Auto Reger&Farm 🔹

Cheapest [proxies and servers](https://proxy-seller.io/?partner=RLLKRCHWGZ90VW) which fits for  on [grass.io](https://app.getgrass.io/register/?referralCode=pti9wWsdR9-wcvD).

![image](https://github.com/MsLolita/grass/assets/58307006/610b95b4-369f-4a71-ac24-f45e8dee6380)


### What is bot for?
   - Create Accounts
   - Farm Points
   - Check Points

> You can put as many proxies as u can, bot uses database and will load up proxies from extra ones

🔹**To say thanks for work: 0x8DD780a898F4B2A01ff121ac07c2d6B47A3E037b**


## Quick Start 📚
   1. To install libraries on Windows click on `INSTALL.bat` (or in console: `pip install -r requirements.txt`).
   2. To start bot use `START.bat` (or in console: `python main.py`).

### Options 📧

1. CREATE ACCOUNTS:
 - In `data/config.py` put `REGISTER_ACCOUNT_ONLY = True`
 - Provide emails and passwords (OPTIONAL) and proxies to register accounts as below!

  ![image](https://github.com/MsLolita/grass/assets/58307006/67740c9b-07d6-4f78-a87d-27b09c0303e8)

2. FARM POINTS:
 - in `data/config.py` put `REGISTER_ACCOUNT_ONLY = False`
 - Provide emails and passwords and proxies to register accounts as shown below!

### Configuration 📧

1. Accounts Setup 🔒

   Put in `data/accounts.txt` accounts in format email:password (cool_aster@gmail.com:my_password123)
   
   ![image](https://github.com/MsLolita/grass/assets/58307006/2f8bacaa-0212-49fe-b362-fe764230f47c)

2. Proxy Setup 🔒

   Configure your proxies with the *ANY* (socks, http/s, ...) format in `data/proxies.txt` 🌐

   ![Proxy Configuration](https://github.com/MsLolita/VeloData/assets/58307006/a2c95484-52b6-497a-b89e-73b89d953d8c)

## Quick Start By Docker
   1. Install Docker-CE: `curl -sSL -k https://get.docker.com | sh`
   2. Install Docker Compose: `curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose`
   3. Clone Source Code: `git clone https://github.com/ChernikovM/GrassAutoFarm.git`
   4. Configuration: Modify `data/accounts.txt` and `data/proxies.txt`
   5. Start Container: `docker-compose up -d`

   PS: Could see more configuration in `docker-compose.yml`

