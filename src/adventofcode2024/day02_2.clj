(ns adventofcode2024.day02
  (:require
    [clojure.string :as str]))

(def sample1
  "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9")

(def input (slurp "resources/input02"))

(defn parse-row [rowstr]
  (map #(Integer/parseInt %) (str/split rowstr #"\s"))
)

(def rows (map parse-row (str/split-lines input)))

(defn safe-gaps?
  [row]
  (let [pairs (partition 2 1 row)]
    (every? #(<= 1 % 3) (map #(abs (- (first %) (last %))) pairs)))
)

(defn ordered?
  [row]
  (or (apply < row) (apply > row))
)

(defn all-variations
  [row]
  (cons row (map 
    #(concat (take % row) (drop (inc %) row))
    (range (count row))))
)

(defn safe?
  [row]
  (and (safe-gaps? row) (ordered? row))
)

(defn safe-variation [row]
  (first (filter safe? (all-variations row))))

(def result (count (keep safe-variation rows)))

(println result)
