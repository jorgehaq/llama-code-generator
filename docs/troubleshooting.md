# 🚨 Troubleshooting – Ollama Local AI

This guide lists common issues and how to fix them when running Ollama locally.

---

## ❌ Error: `"model 'llama2' not found"`

### Cause:
Model has not been downloaded yet.

### Solution:
```bash
ollama pull llama2
```

---

## ❌ Error: `"connection refused"` or port `11434` unreachable

### Cause:

Ollama server is not running or has crashed.

### Solution:

Start the server:

```bash
./scripts/start-ollama.sh
```

Then test:

```bash
curl http://localhost:11434/api/tags
```

---

## ❌ Error: `"address already in use"`

### Cause:

Another Ollama process is already using port 11434.

### Solution:

Check process:

```bash
lsof -i :11434
```

Kill process:

```bash
sudo kill -9 <PID>
```

Then restart.

---

## ❌ Permission Denied on Stop Script

### Cause:

The Ollama process is owned by `ollama` system user, not your current user.

### Solution:

Use `sudo`:

```bash
sudo pkill -u ollama
```

Or stop the system service:

```bash
sudo systemctl stop ollama
```

---

## 📞 Still stuck?

Try these:

```bash
ollama list
ollama show llama2
tail -n 30 ollama.log