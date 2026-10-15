// https://school.programmers.co.kr/learn/courses/30/lessons/42579

class Solution {
    // TODO: 파라미터/리턴타입 문제에 맞게 채우기
    import java.util.*;

class Solution {
    class Song {
        int id;
        int plays;
        
        Song(int id, int plays) {
            this.id = id;
            this.plays = plays;
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> genreTotal = new HashMap<>();
        HashMap<String, List<Song>> genreSongs = new HashMap<>();
        
        for (int i=0; i<genres.length; i++) {
            String genre = genres[i];
            int play = plays[i];
            
            genreTotal.put(
                genre,
                genreTotal.getOrDefault(genre, 0) + play
            );
            
            genreSongs.putIfAbsent(genre, new ArrayList<>());
            genreSongs.get(genre).add(new Song(i, play));
        }
        
        List<String> sortedGenres = new ArrayList<>(genreTotal.keySet());
        // sortedGenres.sort(Comparator.comparingInt((String genre) -> genreTotal.get(genre)).reversed());
        sortedGenres.sort((a,b) ->
            Integer.compare(genreTotal.get(b), genreTotal.get(a))
        );
        
        
        List<Integer> answer = new ArrayList<>();
        
        for (String genre:sortedGenres) {
            List<Song> songs = genreSongs.get(genre);
            
            songs.sort((a,b) -> {
                if (a.plays != b.plays) {
                    return Integer.compare(b.plays, a.plays);
                }
                return Integer.compare(a.id, b.id);
            });
            
            for (int i=0; i<Math.min(2, songs.size()); i++) {
                answer.add(songs.get(i).id);
            }
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution());
    }
}
