# Rapid's Create & Miscellaneous ModPack

A small modpack I made because I was bored and Create is awesome.

I recommend a good enough processor to handle the server and AT MINIMUM 5GB of ram allocated to the server.
I also recommend using a shader. [Complementary Shaders - Reimagined](https://modrinth.com/shader/complementary-reimagined) is a good shader that I recommend.

Step 1: Create a Latest version Forge 1.19.2 Instance<br>
Step 2: Download [Packwiz Installer](https://github.com/packwiz/packwiz-installer-bootstrap/releases) and place it on you instance folder.<br>
Step 3: Edit Instance -> Settings -> Custom Commands, Check the Custom Commands checkbox and paste this in the pre-launch command textbox <code>"$INST_JAVA" -jar $INST_DIR/packwiz-installer-bootstrap.jar https://rapidfuge.github.io/Create-Server-Modpack//pack.toml</code><br>
Step 2: Press launch and profit.<br>
Step 3: Use this docker-compose to easily start a minecraft server.<br>

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
      MEMORY: 5G
      EULA: "TRUE"
      TYPE: "FORGE"
      VERSION: 1.19.2
      FORGE_VERSION: latest
      MOTD: "Rapid's Create & Miscellaneous Server"
      ENABLE_WHITELIST: true
      MODPACK: "https://rapidfuge.github.io/Create-Server-Modpack/pack.toml"
      # If you wish to use a whitelist in the server
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
