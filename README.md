# POC Kubernetes Probes

## Description

Ce projet est un POC qui démontre l'utilisation des mécanismes de health probes dans Kubernetes, notamment les `livenessProbe` et `readinessProbe`.

## Architecture

Le POC est composé de deux microservices :

1. **Service A** : Application Flask qui expose un endpoint `/health` qui communique avec le Service B
2. **Service B** : Application Flask qui expose un endpoint `/hello`

Les deux services sont déployés sur Kubernetes avec des health probes configurées.

## Fonctionnement des probes Kubernetes

Ce POC met en évidence deux types de probes Kubernetes :

- **livenessProbe** : Détermine si un conteneur fonctionne correctement. Si le livenessProbe échoue, Kubernetes redémarre automatiquement le conteneur.
- **readinessProbe** : Détermine si un conteneur est prêt à recevoir du trafic. Si le readinessProbe échoue, le conteneur est temporairement retiré des équilibreurs de charge.

## Configuration Kubernetes

### Service A
- **livenessProbe**: Vérifie l'endpoint `/health` toutes les 10 secondes
- **readinessProbe**: Vérifie l'endpoint `/health` toutes les 10 secondes

### Service B
- **livenessProbe**: Vérifie l'endpoint `/hello` toutes les 10 secondes
- **readinessProbe**: Vérifie l'endpoint `/hello` toutes les 10 secondes

## Scénarios de test

Ce POC permet de tester différents scénarios de défaillance :

1. Ce qui se passe lorsque le Service B tombe en panne (la vérification de santé du Service A échouera et renverra un code 500)
2. Comment Kubernetes gère les redémarrages de conteneurs basés sur les échecs de probes
3. Comment le trafic est routé lorsque les conteneurs ne sont pas prêts

## Déploiement

Les services sont déployés dans le namespace `dma` avec des services de type ClusterIP pour la communication interne.

```bash
kubectl apply -f kubernetes/service-a.yaml
kubectl apply -f kubernetes/service-b.yaml
```
