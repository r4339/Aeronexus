#!/bin/bash

apt-get update -y
apt-get upgrade -y

# Installation des dépendances
apt-get install -y \
    docker.io \
    docker-compose-v2 \
    git \
    nginx \
    python3 \
    python3-pip \
    unzip \
    curl

# Activer Docker
systemctl enable docker
systemctl start docker

# Ajouter ubuntu au groupe docker
usermod -aG docker ubuntu

# Créer le dossier du projet
mkdir -p /opt/aeronexus

# Créer le dossier des logs
mkdir -p /var/log/aeronexus

# Démarrer nginx
systemctl enable nginx
systemctl start nginx

echo "AeroNexus Server Ready" > /opt/aeronexus/status.txt