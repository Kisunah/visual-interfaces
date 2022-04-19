d3.csv('data/showData.csv')
    .then(_data => {
        console.log('Data loading complete');

        let data = _data;

        let characterSelect = document.getElementById('characterSelect');
        characterSelect.addEventListener('change', (event) => {
            const customEvent = new CustomEvent('selectCharacter', { detail: event.target.value });
            document.dispatchEvent(customEvent);
        });

        let episodeSelect = document.getElementById('episodeSelect');
        episodeSelect.addEventListener('change', (event) => {
            const customEvent = new CustomEvent('selectEpisode', { detail: event.target.value });
            document.dispatchEvent(customEvent);
        })

        let mainCharacterList = ['HOUSE', 'WILSON', 'CAMERON', 'CHASE', 'FOREMAN', 'CUDDY', 'KUTNER', 'TAUB', 'THIRTEEN', 'MASTERS', 'ADAMS', 'PARK', 'STACY', 'AMBER']; // Characters with > 250 lines of dialogue

        let characterLineData = {};
        let episodeData = {};
        let timelineData = {};
        timelineData = prepareTimeline(timelineData);

        for (let season in timelineData) {
            for (let episode in timelineData[season]) {
                let option = document.createElement('option');
                option.value = `S${season}E${episode}`;
                option.innerHTML = `S${season}E${episode}`;

                episodeSelect.appendChild(option);
            }
        }

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

            for (let season in episodeData[character]) {
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

        document.addEventListener('selectCharacter', (event) => {
            let character = event.detail;
            characterSelect.value = character;

            let png = ['ADAMS', 'AMBER', 'FOREMAN', 'HOUSE', 'PARK'];
            if (png.indexOf(character) != -1) document.getElementById('characterImage').setAttribute('src', `images/${character}.png`);
            else document.getElementById('characterImage').setAttribute('src', `images/${character}.jpg`);

            let newTimelineData = {};
            newTimelineData = prepareTimeline(newTimelineData);

            data.forEach((item) => {
                let season = parseInt(item.Season);
                let episode = parseInt(item.Episode);

                if (item.Character == character) {
                    if (newTimelineData[season] == undefined) {
                        newTimelineData[season] = {};
                        newTimelineData[season][episode] = 1;
                    } else {
                        if (newTimelineData[season][episode] == undefined) {
                            newTimelineData[season][episode] = 1;
                        } else {
                            newTimelineData[season][episode] += 1;
                        }
                    }
                }
            });

            let newPerEpisodeLineCountData = [];
            for (let season in newTimelineData) {
                for (let episode in newTimelineData[season]) {
                    let obj = {
                        episode: `S${season}E${episode}`,
                        count: newTimelineData[season][episode]
                    };
                    newPerEpisodeLineCountData.push(obj);
                }
            }

            episodeTimeline.updateChart(newPerEpisodeLineCountData);
        });

        let specificEpisodeData = [];

        mainCharacterList.forEach((character) => {
            let obj = {
                character: character,
                count: 0
            };
            specificEpisodeData.push(obj);
        });

        let specificEpisodeChart = new SpecificEpisodeChart({ parentElement: '#specificEpisodeChart' }, specificEpisodeData);

        document.addEventListener('selectEpisode', (event) => {
            episodeSelect.value = event.detail;

            let season = parseInt(event.detail.split('E')[0].split('S')[1]);
            let episode = parseInt(event.detail.split('E')[1]);

            let newSpecificEpisodeData = [];
            let specificEpisodeLineCount = {};

            data.forEach((item) => {
                let itemSeason = parseInt(item.Season);
                let itemEpisode = parseInt(item.Episode);

                if (season == itemSeason && episode == itemEpisode) {
                    if (mainCharacterList.indexOf(item.Character) != -1) {
                        if (specificEpisodeLineCount[item.Character] == undefined) {
                            specificEpisodeLineCount[item.Character] = 1;
                        } else {
                            specificEpisodeLineCount[item.Character] += 1;
                        }
                    }
                }
            });

            mainCharacterList.forEach((character) => {
                let obj = {
                    character: character
                };
                if (specificEpisodeLineCount[character] == undefined) obj['count'] = 0;
                else obj['count'] = specificEpisodeLineCount[character];
                newSpecificEpisodeData.push(obj);
            })
            specificEpisodeChart.updateChart(newSpecificEpisodeData);
        });
    });

// This initializes all episode counts to zero
function prepareTimeline(timelineData) {
    timelineData = {
        1: {
            1: 0
        },
        2: {},
        3: {},
        4: {},
        5: {},
        6: {},
        7: {},
        8: {},
    };

    for (let i = 6; i <= 22; i++) {
        timelineData[1][i] = 0;
    }

    for (let i = 1; i <= 24; i++) {
        timelineData[2][i] = 0;
        timelineData[3][i] = 0;
        timelineData[5][i] = 0;
    }

    for (let i = 1; i <= 16; i++) {
        timelineData[4][i] = 0;
    }

    for (let i = 1; i <= 22; i++) {
        timelineData[6][i] = 0;
        timelineData[8][i] = 0;
    }

    for (let i = 1; i <= 22; i++) {
        if (i != 18) timelineData[7][i] = 0;
    }

    return timelineData;
}

d3.csv('data/cleanedShowData.csv')
    .then(_data => {
        let data = _data;

        let wordData = getWordList(data, 'HOUSE');
        let wordCloud = new WordCloud(wordData[0], wordData[1], 'HOUSE');

        document.addEventListener('selectCharacter', (event) => {
            d3.select('#wordCloud').remove();
            let character = event.detail;
            let newWordData = getWordList(data, character);
            new WordCloud(newWordData[0], newWordData[1], character);
        });
    });

function getWordList(data, character) {
    let limit = 100;
    if (character != 'HOUSE') limit = 25;

    let words = [];
    data.forEach((item) => {
        if (item.Character == character) {
            let wordList = item.Line.split(' ');
            words = words.concat(wordList);
        }
    });

    let wordMap = {};
    words.forEach((word) => {
        if (wordMap[word] == undefined) {
            wordMap[word] = 1;
        } else {
            wordMap[word] += 1;
        }
    });

    let filteredWords = [];
    for (let word in wordMap) {
        if (wordMap[word] > limit) {
            filteredWords.push(word);
        }
    }

    return [filteredWords, wordMap];
}