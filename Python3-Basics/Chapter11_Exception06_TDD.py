# coding=utf-8


def test_is_prime():  # 测试代码
    assert is_prime(5)  # 测试用例
    assert not is_prime(8)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(-3)


def is_prime(number):  # 功能代码（判断指定数字是否为质数）
    if number < 0 or number in (0, 1):
        return False
    for element in range(2, number):
        if number % element == 0:
            return False
    return True


if __name__ == '__main__':
    test_is_prime()  # 执行测试用例

# ### TDD（测试驱动开发）
# 基本思想：开发功能代码前，先开发测试代码，并用测试代码验证功能实现是否满足需求，或者存在缺陷；
# 实现方式：单元测试（被测代码发生改动后，执行单元测试用例验证改动的影响：是否修复缺陷、是否引起回归问题等；
# 简而言之，TDD就是在测试代码的驱动下优化功能代码的开发，其主要实现步骤如下：
# 1. 分析需求；
# 2. 设计测试用例（TDD的核心：开发功能代码前先实现测试代码）；
# 3. 开发测试代码；
# 4. 开发功能代码（使用测试代码验证功能代码，驱动功能完善）：
#    - 4.1 使用测试代码对功能代码进行测试，根据测试结果修复缺陷；
#    - 4.2 重复上一步骤，直到测试用例全部通过（功能实现在有限的测试用例验证下已符合需求)；
