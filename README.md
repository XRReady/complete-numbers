# The Set of Vanished Numbers ($\mathbb{U}$)

This repository contains both the theoretical development and practical implementation of Complete Numbers, a new mathematical structure designed to track information that is lost during multiplication by zero while maintaining computational tractability. Beginning with a foundational singleton set containing a pure zero element, we develop a rigorous framework of mappings that preserve this otherwise lost information.

## Mathematical Foundation

The multiplicative property of zero stands as one of the most fundamental yet peculiar features of computational systems. When a number is multiplied by zero, the result is unambiguous - the product is zero. However, this apparently simple operation masks a subtle but significant loss of information. Consider:

```
5 × 0 = 0
3 × 0 = 0
∴ 5 × 0 = 3 × 0
```

While logically consistent, this sequence demonstrates how distinct numerical values become indistinguishable after multiplication by zero. The complete number system provides a framework that preserves this information while maintaining consistency with standard arithmetic through explicit mappings.

## Implementation

The implementation demonstrates how Complete Numbers can be practically realized in computational systems. The structure parallels complex numbers while preserving information through zero multiplication:

```python
# Complex Number Behavior
z = 3 + 4j
z * 0  -> 0j            # Information lost

# Complete Number Behavior
cu = CompleteNumber(3, 4)
cu * 0 -> 3u + 4uj      # Structure preserved
```

## Interactive Implementation

## Interactive Implementation

Try it yourself: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/12v_dpk2B_MtNzSKA8Lgf9K2neihOHz-e)

The Colab notebook demonstrates the practical implementation of Complete Numbers, allowing you to experiment with the structure and observe how it preserves information through zero multiplication.

> Note: This is a private development version. Public links will be provided upon publication.

## Repository Structure

```
complete-numbers/
├── paper/
│   └── vanished_numbers.pdf    # Mathematical foundation and proofs
├── notebooks/
│   └── complete_numbers_demo.ipynb
├── src/
│   └── complete_numbers.py
└── README.md
```

## Paper Abstract

We introduce a new mathematical structure $\mathbb{U}$, designed to track information that is lost during multiplication by zero while maintaining computational tractability. Beginning with a foundational singleton set containing a pure zero element, we develop a rigorous framework of mappings that preserve this otherwise lost information. The construction provides both theoretical insights into the nature of multiplication by zero and practical applications in computational systems where information preservation is critical. We establish the fundamental properties of $\mathbb{U}$ and demonstrate its relationship to standard number systems through explicit mappings. This work extends naturally to complex numbers and leads to a complete number system that maintains information typically lost in zero multiplication, with applications in data structure design and information theory.

## Paper Status

This work is currently under consideration for publication. The implementation and demonstrations in this repository serve as companion material to the theoretical development presented in the paper.

## Citation

If you use this work in your research, please cite:
```bibtex
@article{spencer2024vanished,
  title={The Set of Vanished Numbers $\mathbb{U}$},
  author={Spencer, Dale},
  year={2024}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
