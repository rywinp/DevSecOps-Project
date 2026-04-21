To run the app locally, you must run

```
$ docker compose up --build
```

to build the image and spin up a container.

To stop the container, do 

```
$ docker compose down
```

### Configure AWS Credentials Stage

- This stage will configure AWS secrets so that our test cases can make requests can be authenticated to our S3 Bucket to validate if changes went through.

### Lint Stage

- Will check our app/main.py and tests/test_main.py files if they adhere to standard code styles. If this fails, then we must refactor our code to make sure that they don't violate any code styles.

### Test Stage

- Will run the six test cases in tests/test_main.py. If any of the test cases fail, then we would need to debug the FastAPI application.

### Build Stage

- Will build the docker image. If this fails, then our dockerfile may be incorrect.

### Security Scan Stage

- Scans our docker image for any vulnerabilities. How Trivy does this is that it checks the image for things like secrets or depedencies that are known to be vulnerable. Trivy uses a vulnerability database to do so. The Report Summary will output all of the dependencies that we have in our image, and if it says that there are any vulnerabilties then we must take action such as replacing the dependency with something more secure.
- A Critical vulnerabiltiy means that there exists an exploit that can cause severe impact such as
  - remote code execution
  - full privilege escalation
  - unauthenticated exploitations over the network
- If the scan fails, then I would adivse the developer to NOT deploy the new changes to production. The developer should find a fix.
