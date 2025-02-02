# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cdbfasta(MakefilePackage):
    """Fast indexing and retrieval of fasta records from flat file databases"""

    homepage = "https://github.com/gpertea/cdbfasta"
    git = "https://github.com/gpertea/cdbfasta.git"

    license("Artistic-2.0")

    version("2017-03-16", commit="b3e481fe02dfbc767a3842bcb1b687c60376a5e8")

    depends_on("cxx", type="build")  # generated

    depends_on("zlib-api")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("cdbfasta", prefix.bin)
        install("cdbyank", prefix.bin)
