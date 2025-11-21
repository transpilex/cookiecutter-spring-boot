package com.example.{{ cookiecutter.project_slug }};

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class {{ cookiecutter.project_slug.title()|replace('-', '')|trim() }}ApplicationTests {

	@Test
	void contextLoads() {
	}

}
