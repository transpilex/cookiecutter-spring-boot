package com.example.{{ cookiecutter.slug }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ cookiecutter.slug.title()|replace('-', '')|trim() }}Application {

	public static void main(String[] args) {
		SpringApplication.run({{ cookiecutter.slug.title()|replace('-', '')|trim() }}Application.class, args);
	}

}
