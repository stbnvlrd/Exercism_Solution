class Translation
  class InvalidCodonError < StandardError
  end
  
  def self.of_codon(codon)
    if codon == 'AUG' then
      return 'Methionine'
    elsif codon == 'UGG' then
      return 'Tryptophan'
    elsif codon == 'UUU' or codon == 'UUC' then
      return 'Phenylalanine'
    elsif codon == 'UUA' or codon == 'UUG' then
      return 'Leucine'
    elsif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' or codon == 'UCG' then
      return 'Serine'
    elsif codon == 'UAA' or codon == 'UAG' or codon == 'UGA' then
      return 'STOP'
    elsif codon == 'UAU' or codon == 'UAC' then
      return 'Tyrosine'
    elsif codon == 'UGU' or codon == 'UGC' then
      return 'Cysteine'
    end
  end

  def self.of_rna(strand)
    translated_strand = []
    number = strand.length / 3
    for index in (0..number-1) do
      codon_translated = Translation.of_codon(strand.slice(3*index, 3))
      if codon_translated == "STOP" then
        return translated_strand
      else
        translated_strand.append(codon_translated)
      end
    end
  return translated_strand
  end
end
