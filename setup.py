import os
import setuptools


with open(f"{os.path.dirname(os.path.abspath(__file__))}/README.md") as readme:
    setuptools.setup(
        name="memory-py",
        version="0.0.1",
        description="Approximate memory usage profiler",
        long_description=readme.read(),
        long_description_content_type="text/markdown",
        author="Vladimir Chebotarev",
        author_email="vladimir.chebotarev@gmail.com",
        license="MIT",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Scientific/Engineering",
            "Topic :: Software Development",
            "Topic :: System :: Benchmark",
            "Topic :: Utilities",
        ],
        keywords=["benchmark", "cpu", "ram", "time", "memory", "heap", "profiling", "valgrind", "massif"],
        project_urls={
            "Documentation": "https://github.com/excitoon/memory/blob/master/README.md",
            "Source": "https://github.com/excitoon/memory",
            "Tracker": "https://github.com/excitoon/memory/issues",
        },
        url="https://github.com/excitoon/memory",
        packages=[],
        scripts=["memory", "memory.cmd"],
        install_requires=["psutil"],
    )
