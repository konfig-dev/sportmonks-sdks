# coding: utf-8

"""
    SportMonks

    Surpass the competition with superior sports data

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

from sportmonks.paths.version_sport_coaches_coach_id.get import CoachById
from sportmonks.paths.version_sport_coaches.get import CoachesAll
from sportmonks.paths.version_sport_coaches_countries_country_id.get import CoachesByCountryId
from sportmonks.paths.version_sport_coaches_latest.get import CoachesLatest
from sportmonks.paths.version_sport_coaches_search_name.get import CoachesSearch
from sportmonks.paths.version_sport_commentaries.get import CommentariesAll
from sportmonks.paths.version_sport_commentaries_fixtures_fixture_id.get import CommentariesByFixtureId
from sportmonks.paths.version_sport_fixtures_between_start_date_end_date_team_id.get import FixtureByDateRangeForTeam
from sportmonks.paths.version_sport_fixtures_fixture_id.get import FixtureById
from sportmonks.paths.version_sport_fixtures.get import FixturesAll
from sportmonks.paths.version_sport_fixtures_date_date.get import FixturesByDate
from sportmonks.paths.version_sport_fixtures_between_start_date_end_date.get import FixturesByDateRange
from sportmonks.paths.version_sport_fixtures_multi_fixture_ids.get import FixturesByIds
from sportmonks.paths.version_sport_fixtures_head_to_head_first_team_second_team.get import FixturesHeadToHead
from sportmonks.paths.version_sport_fixtures_latest.get import FixturesLatest
from sportmonks.paths.version_sport_fixtures_search_name.get import FixturesSearch
from sportmonks.paths.version_sport_leagues_league_id.get import LeagueById
from sportmonks.paths.version_sport_leagues_league_id_includes.get import LeagueEnrichments
from sportmonks.paths.version_sport_leagues_league_id_jerseys.get import LeagueShirts
from sportmonks.paths.version_sport_leagues.get import LeaguesAll
from sportmonks.paths.version_sport_leagues_countries_country_id.get import LeaguesByCountryId
from sportmonks.paths.version_sport_leagues_date_date.get import LeaguesByDate
from sportmonks.paths.version_sport_teams_team_id_leagues.get import LeaguesByTeamId
from sportmonks.paths.version_sport_teams_team_id_leagues_current.get import LeaguesCurrentByTeamId
from sportmonks.paths.version_sport_leagues_live.get import LeaguesLive
from sportmonks.paths.version_sport_leagues_search_name.get import LeaguesSearch
from sportmonks.paths.version_sport_livescores.get import LivescoresAll
from sportmonks.paths.version_sport_livescores_inplay.get import LivescoresAllInPlay
from sportmonks.paths.version_sport_livescores_latest.get import LivescoresLatest
from sportmonks.paths.version_sport_news_post_match.get import NewsAllPostMatch
from sportmonks.paths.version_sport_news_pre_match.get import NewsAllPreMatch
from sportmonks.paths.version_sport_news_post_match_seasons_season_id.get import NewsPostMatchBySeasonId
from sportmonks.paths.version_sport_news_pre_match_seasons_season_id.get import NewsPreMatchBySeasonId
from sportmonks.paths.version_sport_news_post_match_upcoming.get import NewsUpcomingPostMatch
from sportmonks.paths.version_sport_news_pre_match_upcoming.get import NewsUpcomingPreMatch
from sportmonks.paths.version_sport_odds_inplay.get import OddsAllInPlay
from sportmonks.paths.version_sport_odds_pre_match.get import OddsAllPreMatch
from sportmonks.paths.version_sport_odds_inplay_fixtures_fixture_id_bookmakers_bookmaker_id.get import OddsInPlayByFixtureAndBookmakerId
from sportmonks.paths.version_sport_odds_inplay_fixtures_fixture_id_markets_market_id.get import OddsInPlayByFixtureAndMarketId
from sportmonks.paths.version_sport_odds_inplay_fixtures_fixture_id.get import OddsInPlayByFixtureId
from sportmonks.paths.version_sport_odds_inplay_latest.get import OddsLatestInPlay
from sportmonks.paths.version_sport_odds_pre_match_latest.get import OddsLatestPreMatch
from sportmonks.paths.version_sport_odds_pre_match_fixtures_fixture_id_bookmakers_bookmaker_id.get import OddsPreMatchByFixtureAndBookmakerId
from sportmonks.paths.version_sport_odds_pre_match_fixtures_fixture_id_markets_market_id.get import OddsPreMatchByFixtureAndMarketId
from sportmonks.paths.version_sport_odds_pre_match_fixtures_fixture_id.get import OddsPreMatchByFixtureId
from sportmonks.paths.version_sport_players_player_id.get import PlayerById
from sportmonks.paths.version_sport_players.get import PlayersAll
from sportmonks.paths.version_sport_players_countries_country_id.get import PlayersByCountryId
from sportmonks.paths.version_sport_players_latest.get import PlayersLatest
from sportmonks.paths.version_sport_players_search_name.get import PlayersSearch
from sportmonks.paths.version_sport_predictions_probabilities.get import PredictionsAll
from sportmonks.paths.version_sport_predictions_value_bets.get import PredictionsAllValueBets
from sportmonks.paths.version_sport_predictions_probabilities_fixtures_fixture_id.get import PredictionsByFixtureId
from sportmonks.paths.version_sport_predictions_value_bets_fixtures_fixture_id.get import PredictionsValueBetsByFixtureId
from sportmonks.paths.version_sport_referees_referee_id.get import RefereeById
from sportmonks.paths.version_sport_referees.get import RefereesAll
from sportmonks.paths.version_sport_referees_countries_country_id.get import RefereesByCountryId
from sportmonks.paths.version_sport_referees_seasons_season_id.get import RefereesBySeasonId
from sportmonks.paths.version_sport_referees_search_name.get import RefereesSearch
from sportmonks.paths.version_sport_rivals.get import RivalsAll
from sportmonks.paths.version_sport_rivals_teams_team_id.get import RivalsByTeamId
from sportmonks.paths.version_sport_rounds_round_id.get import RoundById
from sportmonks.paths.version_sport_rounds.get import RoundsAll
from sportmonks.paths.version_sport_rounds_seasons_season_id.get import RoundsBySeasonId
from sportmonks.paths.version_sport_rounds_search_name.get import RoundsSearch
from sportmonks.paths.version_sport_schedules_seasons_season_id.get import SchedulesBySeasonId
from sportmonks.paths.version_sport_schedules_seasons_season_id_teams_team_id.get import SchedulesByTeamAndSeasonId
from sportmonks.paths.version_sport_schedules_teams_team_id.get import SchedulesByTeamId
from sportmonks.paths.version_sport_seasons_season_id.get import SeasonById
from sportmonks.paths.version_sport_seasons.get import SeasonsAll
from sportmonks.paths.version_sport_seasons_teams_team_id.get import SeasonsByTeamId
from sportmonks.paths.version_sport_seasons_search_name.get import SeasonsSearch
from sportmonks.paths.version_sport_squads_seasons_season_id_teams_team_id.get import SquadsBySeasonAndTeamId
from sportmonks.paths.version_sport_squads_teams_team_id.get import SquadsByTeamId
from sportmonks.paths.version_sport_stages_stage_id.get import StageById
from sportmonks.paths.version_sport_stages.get import StagesAll
from sportmonks.paths.version_sport_stages_seasons_season_id.get import StagesBySeasonId
from sportmonks.paths.version_sport_stages_search_name.get import StagesSearch
from sportmonks.paths.version_sport_standings_corrections_seasons_season_id.get import StandingCorrectionsBySeasonId
from sportmonks.paths.version_sport_standings.get import StandingsAll
from sportmonks.paths.version_sport_standings_rounds_round_id.get import StandingsByRoundId
from sportmonks.paths.version_sport_standings_seasons_season_id.get import StandingsBySeasonId
from sportmonks.paths.version_sport_standings_live_leagues_league_id.get import StandingsLiveByLeagueId
from sportmonks.paths.version_sport_states_state_id.get import StateById
from sportmonks.paths.version_sport_states.get import StatesBySport
from sportmonks.paths.version_sport_teams.get import TeamsAll
from sportmonks.paths.version_sport_teams_countries_country_id.get import TeamsByCountryId
from sportmonks.paths.version_sport_teams_team_id.get import TeamsById
from sportmonks.paths.version_sport_teams_seasons_season_id.get import TeamsBySeasonId
from sportmonks.paths.version_sport_teams_search_name.get import TeamsSearch
from sportmonks.paths.version_sport_topscorers_seasons_season_id.get import TopScorersBySeasonId
from sportmonks.paths.version_sport_topscorers_stages_stage_id.get import TopScorersByStageId
from sportmonks.paths.version_sport_transfers_between_start_date_end_date.get import TranfersByDateRange
from sportmonks.paths.version_sport_transfers_transfer_id.get import TransferById
from sportmonks.paths.version_sport_transfers.get import TransfersAll
from sportmonks.paths.version_sport_transfers_players_player_id.get import TransfersByPlayerId
from sportmonks.paths.version_sport_transfers_teams_team_id.get import TransfersByTeamId
from sportmonks.paths.version_sport_transfers_latest.get import TransfersLatest
from sportmonks.paths.version_sport_tv_stations_tv_station_id.get import TvStationById
from sportmonks.paths.version_sport_tv_stations.get import TvStationsAll
from sportmonks.paths.version_sport_tv_stations_fixtures_fixture_id.get import TvStationsByFixtureId
from sportmonks.paths.version_sport_venues_venue_id.get import VenueById
from sportmonks.paths.version_sport_venues.get import VenuesAll
from sportmonks.paths.version_sport_venues_seasons_season_id.get import VenuesBySeasonId
from sportmonks.paths.version_sport_venues_search_name.get import VenuesSearch


class SportApi(
    CoachById,
    CoachesAll,
    CoachesByCountryId,
    CoachesLatest,
    CoachesSearch,
    CommentariesAll,
    CommentariesByFixtureId,
    FixtureByDateRangeForTeam,
    FixtureById,
    FixturesAll,
    FixturesByDate,
    FixturesByDateRange,
    FixturesByIds,
    FixturesHeadToHead,
    FixturesLatest,
    FixturesSearch,
    LeagueById,
    LeagueEnrichments,
    LeagueShirts,
    LeaguesAll,
    LeaguesByCountryId,
    LeaguesByDate,
    LeaguesByTeamId,
    LeaguesCurrentByTeamId,
    LeaguesLive,
    LeaguesSearch,
    LivescoresAll,
    LivescoresAllInPlay,
    LivescoresLatest,
    NewsAllPostMatch,
    NewsAllPreMatch,
    NewsPostMatchBySeasonId,
    NewsPreMatchBySeasonId,
    NewsUpcomingPostMatch,
    NewsUpcomingPreMatch,
    OddsAllInPlay,
    OddsAllPreMatch,
    OddsInPlayByFixtureAndBookmakerId,
    OddsInPlayByFixtureAndMarketId,
    OddsInPlayByFixtureId,
    OddsLatestInPlay,
    OddsLatestPreMatch,
    OddsPreMatchByFixtureAndBookmakerId,
    OddsPreMatchByFixtureAndMarketId,
    OddsPreMatchByFixtureId,
    PlayerById,
    PlayersAll,
    PlayersByCountryId,
    PlayersLatest,
    PlayersSearch,
    PredictionsAll,
    PredictionsAllValueBets,
    PredictionsByFixtureId,
    PredictionsValueBetsByFixtureId,
    RefereeById,
    RefereesAll,
    RefereesByCountryId,
    RefereesBySeasonId,
    RefereesSearch,
    RivalsAll,
    RivalsByTeamId,
    RoundById,
    RoundsAll,
    RoundsBySeasonId,
    RoundsSearch,
    SchedulesBySeasonId,
    SchedulesByTeamAndSeasonId,
    SchedulesByTeamId,
    SeasonById,
    SeasonsAll,
    SeasonsByTeamId,
    SeasonsSearch,
    SquadsBySeasonAndTeamId,
    SquadsByTeamId,
    StageById,
    StagesAll,
    StagesBySeasonId,
    StagesSearch,
    StandingCorrectionsBySeasonId,
    StandingsAll,
    StandingsByRoundId,
    StandingsBySeasonId,
    StandingsLiveByLeagueId,
    StateById,
    StatesBySport,
    TeamsAll,
    TeamsByCountryId,
    TeamsById,
    TeamsBySeasonId,
    TeamsSearch,
    TopScorersBySeasonId,
    TopScorersByStageId,
    TranfersByDateRange,
    TransferById,
    TransfersAll,
    TransfersByPlayerId,
    TransfersByTeamId,
    TransfersLatest,
    TvStationById,
    TvStationsAll,
    TvStationsByFixtureId,
    VenueById,
    VenuesAll,
    VenuesBySeasonId,
    VenuesSearch,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
