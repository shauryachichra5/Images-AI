# Images AI 🚀
The aim of the project is to test out deployment (Render for now..), docker and fast-api.

---

## Hosted the project using Render
Try it yourself -> https://images-ai-wz6g.onrender.com

---

### **Getting Started** (Using Docker)
Test **ImagesAI V1** using Docker in just a few simple steps.

1. **Install Docker** and log in to your Docker account.
2. **Create a `.env` file** using the template provided in the repository.
3. **Pull the Docker image**:

```bash
docker pull shauryachichra/imagesai:v1
```
4. **Run the Container** by attaching your `.env`
```
docker run --env-file .env -p 8000:8000 shauryachichra/imagesai:v1
```
⚠️ Note: This is a beta version for testing and learning Docker and FastAPI.
