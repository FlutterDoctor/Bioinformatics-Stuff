# Problem

# For positive integers a and n, a modulo n (written amodn in shorthand) is the remainder when a is divided by n. For example, 29mod11=7 because 29=11×2+7.

# Modular arithmetic is the study of addition, subtraction, multiplication, and division with respect to the modulo operation. We say that a and b are congruent modulo n if amodn=bmodn; in this case, we use the notation a≡bmodn.

# Two useful facts in modular arithmetic are that if a≡bmodn and c≡dmodn, then a+c≡b+dmodn and a×c≡b×dmodn. To check your understanding of these rules, you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11.

# As you will see in this exercise, some Rosalind problems will ask for a (very large) integer solution modulo a smaller number to avoid the computational pitfalls that arise with storing such large numbers.

# Given: A protein string of length at most 1000 aa.

# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

# :::::::::::::::::::::::::::::::: SOLUTION :::::::::::::::::::::::::::::::::::::::
def count_rna_strings(protein):
    codon_table = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
        'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    }
    num_rna_strings = 3  # start with 3 for the stop codons

    for aa in protein:
        num_rna_strings *= codon_table[aa]
        num_rna_strings %= 1_000_000  # apply modulo to avoid large numbers

    return num_rna_strings

protein = "MTYMVGCFMYRTGPIKFEPKHEGGLPVEKTHVCAQQMKRLWDSAVPRADVNCPPPIVYEARNGYIAEHALLVMAVTHESVCKRAVLECAHLQYHRPVQPIIHTQSYSEPWNLESYCATHNDWEVVWWKGGEVFNMNYLEFPYTCYEPSVYEGQQCQNDATPCNTVLQDLKKVVFQMDIDKDWPCTMSAPGAGANQRVVFFNYHRDTVYQIIKRVVPIPWIGGWFGWDLRGWRCKFQPTYPWKMYHVYCKCHVGQQWNWQTKMAKVHCSTNLCFCWNPVCSVRQMSNFCPMYMSHTYKLWAKFVIIFYHTKEIILNEQTQWEQYVRGFRINQKQVAILNNNHGRMDTHRVFDGHCNKDVQNSAVDNETDEYSEHFTIVRKCYVMVKFSCFERSGEGCLQTMFIRCEPPNQEAVHLNGSYCGNMQNRVYTIDWLQNPWYGGMMEAFTWADMAYLEPQAASQSPWCPYCECRTAWPWCAMTIVCGAAPSYGNLGFFWKNGDCKLRRKGMCFPVNSVDAGWLGVEAPAQDAFLIQGENCNNNFFKLCPWSLSKNMACEDMWVGWHAAPKGMPIHNGKRSCIEDTMLWSDYPCMACVFCKPYHIAILNYGVAKRNSVGLSYYLQCMLRDYYWRTWAFMFWCCEGWCWMMEIGLHPGWYKWEKHICWNPGTQAASQAHVMGNVDDGCMFKNSSKCHNWFHFVIKHNLIHTRNCCGYQCANRVHLKFEYPEGICLMDVQPQWLSDIVAFHNRIQIRGLDQMVLFDHTARFIIAFEEWHNQIKGQIIWGLDTECMPISKFQHCLRTHQPLVLKESDCKGPPAAGHIGSIKFRARKGWFMKHAANPAKVNYFVNRSHQFCVLPKAILSIWTCFGVCWLQMDGKKCFNVPFHEMKSVCMGVYLVSSCQLTRWPQNPDVNNFGNCDPDNSRYWDNECCCWLGMPIPYYCETKNINDTLASIPGFNFMPFMCWDGYIQMYPWMIWCWENHTIPKGHVDEEYYARAANRMFKR"
print(count_rna_strings(protein))  
