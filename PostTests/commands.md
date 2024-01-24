# Windows 
## Install k6
```bash
winget install k6 --source winget
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
