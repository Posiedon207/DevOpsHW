FROM eclipse-temurin:17-jdk-alpine AS builder
WORKDIR /app
COPY HelloWorld.java .
RUN javac HelloWorld.java

FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY --from=builder /app/HelloWorld.class .
EXPOSE 8080
CMD ["java", "HelloWorld"]
