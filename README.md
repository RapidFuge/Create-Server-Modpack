# Rapid's Create & Miscellaneous ModPack
A small modpack I made because I was bored and Create is awesome.

There is a possibility that you may need 5GB of ram to run the modpack. But you may experiment with 4GB. I also recommend a good enough processor to handle the server.
I also recommend using a shader. [Complementary Shaders - Reimagined](https://modrinth.com/shader/complementary-reimagined) is a good shader that I recommend.

Step 1: Download the Client mods, and Resource Pack (optional) from the [releases](https://github.com/RapidFuge/Create-Server-Modpack/releases/latest) section.<br>
Step 2: Use MultiMC or Prism Launcher to create a minecraft instance that is 1.19.2 and the most latest Forge version. and import the client mods in the instance.<br>
Step 3: Use this docker-compose to easily start a minecraft server.
```yaml
services:
  minecraft:
    image: itzg/minecraft-server
    container_name: minecraft
    tty: true
    stdin_open: true
    ports:
      - "25565:25565"
    environment:
      MEMORY: 4G
      EULA: "TRUE"
      TYPE: "FORGE"
      VERSION: 1.19.2
      FORGE_VERSION: latest
      MOTD: "Rapid's Create & Miscellaneous Server"
      ENABLE_WHITELIST: true
      # NOTE: to use a resource pack, you need to input in a LINK and not a FILE PATH.
      RESOURCE_PACK: "https://github.com/rapidfuge/create-server-modpack/releases/latest/download/resource-pack.zip"
      # NOTE: server-mods.zip must be in the same directory as the server directory OR a URL LINK.
      MODPACK: "https://github.com/rapidfuge/create-server-modpack/releases/latest/download/server-mods.zip"
      CUSTOM_SERVER_PROPERTIES: |
        resource-pack-prompt=true
        max-tick-time=-1
      WHITELIST: |
        Playername
      OPS: |
        Playername
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
  #   # POST_BACKUP_SCRIPT_FILE: /post-backup.sh
  #   volumes:
  #     - ./server:/data:ro
  #     - ./mc-backups:/backups
  #     # - ./post-backup.sh:/post-backup.sh:ro
```
Then just do the command <code>docker-compose up -d</code> To start the server!
