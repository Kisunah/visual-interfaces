d3.csv('data/showData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let mainCharacterList = ['HOUSE', 'WILSON', 'CAMERON', 'CHASE', 'FOREMAN', 'CUDDY', 'KUTNER', 'TAUB', 'THIRTEEN', 'MASTERS', 'ADAMS', 'PARK', 'STACY', 'AMBER']; // Characters with > 250 lines of dialogue



        let characterLineData = {};
        let episodeData = {};
        let timelineData = {
            1: {
                1: 0,
                6: 0,
                7: 0,
                8: 0,
                9: 0,
                10: 0,
                11: 0
            }
        };

        data.forEach((item) => {
            let season = parseInt(item.Season);
            let episode = parseInt(item.Episode);

            if (characterLineData[item.Character] == undefined) characterLineData[item.Character] = 1;
            else characterLineData[item.Character] += 1;

            if (mainCharacterList.indexOf(item.Character) != -1) {
                if (episodeData[item.Character] == undefined) {
                    episodeData[item.Character] = {};
                    episodeData[item.Character][season] = [episode];
                } else {
                    if (episodeData[item.Character][season] == undefined) {
                        episodeData[item.Character][season] = [episode]
                    } else {
                        if (episodeData[item.Character][season].indexOf(episode) == -1) {
                            episodeData[item.Character][season].push(episode);
                        }
                    }
                }
            }

            if (item.Character == 'HOUSE') {
                if (timelineData[season] == undefined) {
                    timelineData[season] = {};
                    timelineData[season][episode] = 1;
                } else {
                    if (timelineData[season][episode] == undefined) {
                        timelineData[season][episode] = 1;
                    } else {
                        timelineData[season][episode] += 1;
                    }
                }
            }
        });

        let temp = [];
        mainCharacterList.forEach((character) => {
            let obj = {
                character: character,
                count: characterLineData[character]
            };
            temp.push(obj);
        });
        characterLineData = temp;

        let characterLineCountChart = new CharacterLineCountChart({ parentElement: '#characterLineCountChart' }, characterLineData);


        let characterEpisodeCountData = [];
        mainCharacterList.forEach((character) => {
            let obj = {
                character: character,
                count: 0
            };
            let episodeCount = 0;

            for(let season in episodeData[character]) {
                episodeCount += episodeData[character][season].length;
            }
            obj.count = episodeCount;
            characterEpisodeCountData.push(obj);
        });

        let characterEpisodeCountChart = new CharacterEpisodeCountChart({ parentElement: '#characterEpisodeCountChart' }, characterEpisodeCountData);

        let perEpisodeLineCountData = [];
        for (let season in timelineData) {
            for (let episode in timelineData[season]) {
                let obj = {
                    episode: `S${season}E${episode}`,
                    count: timelineData[season][episode]
                };
                perEpisodeLineCountData.push(obj);
            }
        }

        let episodeTimeline = new EpisodeTimeline({ parentElement: '#episodeTimeline' }, perEpisodeLineCountData);
    });