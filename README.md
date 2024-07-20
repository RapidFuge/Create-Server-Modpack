# Rapid's Create & Miscellaneous ModPack
A small modpack I made because I was bored and Create is awesome.

Step 1: Download the Client, Server, and Resource Pack (optional) from the [releases](https://github.com/RapidFuge/Create-Server-Modpack/releases/latest) section.
Step 2: Use MultiMC or Prism Launcher to create a minecraft instance that is 1.18.2 and the most latest Forge launcher or 40.2.4 to newer versions. and import the client mods in the instance.
Step 3: Use this docker-compose to easily start a minecraft server.
```yaml
services:
  mc:
    image: itzg/minecraft-server
    tty: true
    stdin_open: true
    ports:
      - "25565:25565"
    environment:
      MEMORY: 3G
      EULA: "TRUE"
      TYPE: "FORGE"
      VERSION: 1.18.2
      FORGE_VERSION: latest
      MOTD: "Rapid's Create & Miscellaneous Server"
      ENABLE_WHITELIST: true
      # NOTE: resource-pack.zip and server-mods.zip must be in the same directory as the server directory.
      RESOURCE_PACK: "./resource-pack.zip"
      MODPACK: "./server-mods.zip"
      CUSTOM_SERVER_PROPERTIES: |
        resource-pack-prompt=true
      WHITELIST: |
        RapidFuge
      OPS: |
        RapidFuge
    volumes:
      - ./server:/data

  # Manual Backups sub-container to backup the server.
  # backups:
  #   image: itzg/mc-backup
  #   environment:
  #     BACKUP_INTERVAL: "1h"
  #     RCON_HOST: mc
  #     PRE_BACKUP_SCRIPT: |
  #       echo "Before backup!"
  #       echo "Also before backup from $$RCON_HOST to $$DEST_DIR"
  #     POST_BACKUP_SCRIPT_FILE: /post-backup.sh
  #   volumes:
  #     - ./Actual Server:/data:ro
  #     - ./mc-backups:/backups
  #     # - ./post-backup.sh:/post-backup.sh:ro
```
Then just do the command <code>docker-compose up -d</code> To start the server!
