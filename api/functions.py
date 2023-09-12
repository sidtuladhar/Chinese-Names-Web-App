import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

pkg = "ChineseNames"
importr(pkg)


def compute_name(name, year):
    return robjects.r.compute_name_index(name=name, birth=year)


if __name__ == '__main__':
    result = compute_name('包寒吴霜', 1995)
    print(result)
    SNU = result[7][0]
    SNI = result[8][0]
    NU = result[9][0]
    CCU = result[10][0]
    NG = result[11][0]
    NV = result[12][0]
    NW = result[13][0]
    NC = result[14][0]

    print(SNU, SNI, NU, CCU, NG, NV, NW, NC)
