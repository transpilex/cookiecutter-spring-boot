package com.example.{{ cookiecutter.slug }};

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class {{ cookiecutter.slug.title()|replace('-', '')|trim() }}ApplicationTests {

	@Test
	void contextLoads() {
	}

}
