package com.example.{{ cookiecutter.slug }};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class {{ cookiecutter.application_class }} {

	public static void main(String[] args) {
		SpringApplication.run({{ cookiecutter.application_class }}.class, args);
	}

}
