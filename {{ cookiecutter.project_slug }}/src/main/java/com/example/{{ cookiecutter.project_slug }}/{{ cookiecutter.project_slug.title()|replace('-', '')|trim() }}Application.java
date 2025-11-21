package com.example.{{ cookiecutter.project_slug }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ cookiecutter.project_slug.title()|replace('-', '')|trim() }}Application {

	public static void main(String[] args) {
		SpringApplication.run({{ cookiecutter.project_slug.title()|replace('-', '')|trim() }}Application.class, args);
	}

}
