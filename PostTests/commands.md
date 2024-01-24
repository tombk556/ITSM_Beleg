# Install k6
[Installation Guide](https://grafana.com/docs/k6/latest/get-started/installation/)

## Windows 
```bash
winget install k6 --source winget
```

## MacOS
```bash
brew install k6
```

## Docker
```bash
docker pull grafana/k6
```

# Run Tests

## Load-Test
```bash
cat PostTests/loadtest.js | docker run --rm -i grafana/k6 run -
```

## Integration-Test
```bash
cat PostTests/integrationtest.js | docker run --rm -i grafana/k6 run
```
