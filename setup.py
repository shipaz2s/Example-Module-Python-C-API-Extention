from setuptools import Extension, setup

setup(
	ext_modules=[
		Extension(
			name="custom",  # as it would be imported
							# may include packages/namespaces separated by `.`

			sources=["custom.c"], # all sources are compiled into a single binary file
			language="c",
		),
	]
)