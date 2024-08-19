def gen_soft(software, version=None):
    soft = ""
    if software["source"] == "github":
        soft += (
            f'RUN git clone https://github.com/{software["user"]}/{software["repo"]}\n'
        )
        soft += f'WORKDIR /root/{software["repo"]}\n'
        if version is not None:
            soft += f"RUN git checkout {version}\n"
    elif software["source"] == "tarball":
        soft += f'RUN wget {software["url"]}\n'
        soft += f'RUN unzip {software["name"]}.zip\n'
        soft += f'WORKDIR /root/{software["name"]}\n'
    elif software["source"] == "targz":
        soft += f'RUN wget {software["url"]}\n'
        soft += f'RUN tar -xzvf {software["name"]}.tar.gz\n'
        soft += f'WORKDIR /root/{software["name"]}\n'
    elif software["source"] == "gz":
        soft += f'RUN wget {software["url"]}\n'
        soft += f'RUN tar -xvf {software["name"]}.gz\n'
        soft += f'WORKDIR /root/{software["name"]}\n'
    elif software["source"] == "tgz":
        soft += f'RUN wget {software["url"]}\n'
        soft += f'RUN tar -xvf {software["name"]}.tgz\n'
        soft += f'WORKDIR /root/{software["name"]}\n'
    elif software["source"] == "tarbz2":
        soft += f'RUN wget {software["url"]}\n'
        soft += f'RUN tar -xvf {software["name"]}.tar.bz2\n'
        soft += f'WORKDIR /root/{software["name"]}\n'
    return soft
