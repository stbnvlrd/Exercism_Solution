class Translation
    def self.of_codon(strand)
      translated_strand = []
      number = strand.length / 3
      for index in (0..number) do
        codon = strand[index*3..(index*6)-1]
        if codon == 'AUG' then
          translated_strand.append('Methionine')
        elsif codon == 'UGG' then
          translated_strand.append('Tryptophan')
        elsif codon == 'UUU' or codon == 'UUC' then
          translated_strand.append('Phenylalanine')
        elsif codon == 'UUA' or codon == 'UUG' then
          translated_strand.append('Leucine')
        elsif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' then
          translated_strand.append('Serine')
        elsif codon == 'UAA' or codon == 'UAG' or codon == 'UGA' then
          translated_strand.append('STOP')
        elsif codon == 'UAU' or codon == 'UAC' then
          translated_strand.append('Tyrosine')
        elsif codon == 'UGU' or codon == 'UGC' then
          translated_strand.append('Cysteine')
        end
      end
      return translated_strand.join(" ")
    end
