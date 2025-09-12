# Images AI 🚀

Test **ImagesAI V1** using Docker in just a few simple steps.

---

## Hosted the project using Render
Try it yourself -> https://images-ai-wz6g.onrender.com

---

### **Getting Started**

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
